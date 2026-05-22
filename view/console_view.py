import os
import sys
import time
import shutil
from model.menu_model import Menu

# ANSI color constants
RESET  = "\033[0m"
CYAN   = "\033[96m"   # panel titles
WHITE  = "\033[97m"   # options and content
RED    = "\033[91m"   # option 0 exit/back
YELLOW = "\033[93m"   # input prompt
GREEN  = "\033[92m"   # output results
GRAY   = "\033[37m"   # placeholder text
BLUE   = "\033[34m"   # frame borders + selected block title
DIM    = "\033[90m"   # unselected blocks when one is active


class ConsoleView:
    """Three-panel dynamic layout that fills the real terminal size.

    Structure (6 fixed rows + content_rows):
      row 1          : top border   (+===+===+===+)
      row 2          : headers      (|   |   |   |)
      row 3          : header sep   (|---+---+---|)
      rows 4..3+CR   : content      (|   |   |   |)  CR = rows - 5
      row 4+CR       : mid border   (+===========+)
      row 5+CR       : input bar    (|           |)

    Column positions (1-based, left edge = col 1):
      left panel  content : col 2
      center panel content: col L+3
      right panel content : col L+C+4
    """

    def gotoxy(self, x: int, y: int) -> None:
        """Move cursor to column x, row y (1-based ANSI)."""
        print(f"\033[{y};{x}H", end="", flush=True)

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def _dims(self) -> tuple[int, int, int, int]:
        """Return (L, C, R, CR) computed from current terminal size.

        L  = left panel content width  (~25 % of cols)
        C  = center panel content width (~40 % of cols)
        R  = right panel content width (remainder after 4 border chars)
        CR = content rows (rows - 5 overhead rows)
        """
        cols, rows = shutil.get_terminal_size(fallback=(120, 30))
        L  = int(cols * 0.25)
        C  = int(cols * 0.40)
        R  = cols - 4 - L - C   # 4 border chars: | | | |
        CR = rows - 5            # overhead: top + header + sep + mid + input
        return L, C, R, CR

    @staticmethod
    def _fit(text: str, width: int) -> str:
        """Pad/truncate plain text to exactly `width` visible characters."""
        if len(text) > width:
            text = text[:width - 3] + "..."
        return text.ljust(width)[:width]

    # ── one-time layout draw ──────────────────────────────────────────────

    def draw_layout(self) -> None:
        """Clear screen and draw all borders + headers once.
        Never call again; only panel contents change afterwards."""
        self.clear()
        L, C, R, CR = self._dims()
        IW = L + 1 + C + 1 + R   # inner width shared by mid-border and input bar

        def p(x: int, y: int, text: str) -> None:
            self.gotoxy(x, y)
            print(text, end="", flush=True)

        # row 1 — top border
        p(1, 1, BLUE + "+" + "="*L + "+" + "="*C + "+" + "="*R + "+" + RESET)

        # row 2 — panel headers
        p(1, 2,
          BLUE+"|"+RESET + CYAN+"BLOQUES".center(L)+RESET
          + BLUE+"|"+RESET + CYAN+"GUIA PRACTICA 1".center(C)+RESET
          + BLUE+"|"+RESET + CYAN+"EJERCICIOS".center(R)+RESET
          + BLUE+"|"+RESET)

        # row 3 — header separator
        p(1, 3, BLUE + "|" + "-"*L + "+" + "-"*C + "+" + "-"*R + "|" + RESET)

        # rows 4..3+CR — empty content rows
        blank = (BLUE+"|"+RESET+" "*L + BLUE+"|"+RESET+" "*C
                 + BLUE+"|"+RESET+" "*R + BLUE+"|"+RESET)
        for i in range(CR):
            p(1, 4 + i, blank)

        # row 4+CR — mid border (full span)
        p(1, 4 + CR, BLUE + "+" + "="*IW + "+" + RESET)

        # row 5+CR — input bar
        p(1, 5 + CR, BLUE + "|" + RESET + " "*IW + BLUE + "|" + RESET)

        self.update_exercises_panel("", [])
        self.update_output_panel("")

    # ── panel updaters ────────────────────────────────────────────────────

    def update_blocks_panel(self, blocks: list[str], selected_index: int = -1) -> None:
        """Overwrite left panel content only — borders stay untouched."""
        L, _, _, CR = self._dims()
        col = 2   # sx(1) + left border(1)

        for i in range(CR):
            self.gotoxy(col, 4 + i)
            if i < len(blocks):
                raw  = f"{i + 1}. {blocks[i]}"
                pfx  = "-> " if i == selected_index else "   "
                cell = self._fit(pfx + raw, L)
                if selected_index == -1:
                    color = WHITE
                elif i == selected_index:
                    color = CYAN
                else:
                    color = DIM
            else:
                cell, color = " " * L, WHITE
            print(color + cell + RESET, end="", flush=True)

    def update_exercises_panel(self, title: str, exercises: list[str]) -> None:
        """Overwrite center panel content only — borders stay untouched."""
        L, C, _, CR = self._dims()
        col = L + 3   # sx(1) + left border(1) + L + divider(1)
        mid = CR // 2

        for i in range(CR):
            self.gotoxy(col, 4 + i)

            if not title:
                if i == mid:
                    print(GRAY + "<- selecciona un bloque".center(C)[:C] + RESET,
                          end="", flush=True)
                else:
                    print(" " * C, end="", flush=True)
                continue

            if i == 0:
                print(BLUE + self._fit(" " + title, C) + RESET, end="", flush=True)
            elif i == 1:
                print(BLUE + self._fit(" " + "-" * (C - 2), C) + RESET, end="", flush=True)
            else:
                ex = i - 2
                if ex < len(exercises):
                    print(WHITE + self._fit(f"  {ex + 1}. {exercises[ex]}", C) + RESET,
                          end="", flush=True)
                elif ex == len(exercises) + 1:
                    print(RED + self._fit("  0. Volver", C) + RESET, end="", flush=True)
                else:
                    print(" " * C, end="", flush=True)

    def update_output_panel(self, output: str) -> None:
        """Overwrite right panel content only — borders stay untouched."""
        L, C, R, CR = self._dims()
        col   = L + C + 4   # sx(1) + border(1) + L + div(1) + C + div(1)
        lines = output.splitlines() if (output and output.strip()) else []
        mid   = CR // 2

        for i in range(CR):
            self.gotoxy(col, 4 + i)
            if not lines:
                if i == mid:
                    print(GRAY + "<- selecciona un".center(R)[:R] + RESET, end="", flush=True)
                elif i == mid + 1:
                    print(GRAY + "   ejercicio".center(R)[:R] + RESET, end="", flush=True)
                else:
                    print(" " * R, end="", flush=True)
            elif i < len(lines):
                print(GREEN + lines[i][:R].ljust(R) + RESET, end="", flush=True)
            else:
                print(" " * R, end="", flush=True)

    # ── input bar ─────────────────────────────────────────────────────────

    def get_selection(self, prompt: str = "Selecciona una opcion") -> str:
        """Read input key-by-key so the cursor never leaves the input bar row."""
        L, C, R, CR = self._dims()
        IW    = L + 1 + C + 1 + R
        row   = 5 + CR
        chars: list[str] = []

        while True:
            # Redraw the bar with whatever has been typed so far
            self.gotoxy(2, row)
            print(" " * IW, end="", flush=True)
            self.gotoxy(2, row)
            current = "".join(chars)
            print(YELLOW + f" {prompt}: " + RESET + WHITE + current + RESET,
                  end="", flush=True)

            if os.name == "nt":                  # Windows
                import msvcrt
                ch = msvcrt.getwch()
                if ch in ("\r", "\n"):           # Enter
                    break
                elif ch == "\b":                 # Backspace
                    if chars:
                        chars.pop()
                elif ch.isprintable():
                    chars.append(ch)
            else:                                # Linux / Mac
                import tty, termios
                fd  = sys.stdin.fileno()
                old = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old)
                if ch in ("\r", "\n"):
                    break
                elif ch == "\x7f":               # Backspace on Linux/Mac
                    if chars:
                        chars.pop()
                elif ch.isprintable():
                    chars.append(ch)

        return "".join(chars).strip()

    def show_error(self, message: str) -> None:
        """Display an error message in the input bar for 2 seconds, then clear it."""
        L, C, R, CR = self._dims()
        IW  = L + 1 + C + 1 + R
        row = 5 + CR
        self.gotoxy(2, row)
        print(" " * IW, end="", flush=True)
        self.gotoxy(2, row)
        print(RED + message[:IW].ljust(IW) + RESET, end="", flush=True)
        time.sleep(2)
        self.gotoxy(2, row)
        print(" " * IW, end="", flush=True)
        self.gotoxy(2, row)

    # ── legacy stubs (kept so nothing external breaks) ────────────────────

    def display_menu(self, _menu: Menu) -> None:
        pass

    def display_output(self, _output: str) -> None:
        pass

    def wait_for_user(self) -> None:
        pass
