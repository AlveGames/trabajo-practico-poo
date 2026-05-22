from model.block_manager import BlockManager
from view.console_view import ConsoleView


class AppController:
    """Connects BlockManager and ConsoleView in a three-panel static layout."""

    def __init__(self, manager: BlockManager, view: ConsoleView):
        self.manager = manager
        self.view    = view

    # ── helpers ───────────────────────────────────────────────────────────

    def _titles(self) -> list[str]:
        return [b.title for b in self.manager.blocks.values()]

    def _names(self) -> list[str]:
        return list(self.manager.blocks.keys())

    # ── main loop ─────────────────────────────────────────────────────────

    def run(self) -> None:
        """Draw layout once, then loop on block selection."""
        self.view.clear()
        self.view.draw_layout()

        titles    = self._titles()
        names     = self._names()
        main_menu = self.manager.get_main_menu()

        self.view.update_blocks_panel(titles)

        while True:
            choice = self.view.get_selection("Bloque (0 = Cerrar Terminal)")

            if not choice or not choice.isdigit():
                self.view.show_error("Solo se permiten números. Intenta de nuevo.")
                continue

            if not main_menu.is_valid_choice(choice):
                total = len(main_menu.options)
                self.view.show_error(f"Opción inválida. Ingresa un número entre 1 y {total}.")
                continue

            if choice == "0":
                self.view.clear()
                break

            idx = int(choice) - 1
            self.view.update_blocks_panel(titles, idx)
            self._run_block(names[idx])

    # ── block sub-loop ────────────────────────────────────────────────────

    def _run_block(self, block_name: str) -> None:
        """Show exercises for a block, run chosen one, display output."""
        block      = self.manager.blocks[block_name]
        block_menu = self.manager.get_block_menu(block_name)

        self.view.update_exercises_panel(block.title, block.exercises)
        self.view.update_output_panel("")

        while True:
            choice = self.view.get_selection("Ejercicio (0=Volver)")

            if not choice or not choice.isdigit():
                self.view.show_error("Solo se permiten números. Intenta de nuevo.")
                continue

            if not block_menu.is_valid_choice(choice):
                total = len(block_menu.options)
                self.view.show_error(f"Opción inválida. Ingresa un número entre 1 y {total}.")
                continue

            if choice == "0":
                self.view.update_blocks_panel(self._titles(), -1)
                self.view.update_exercises_panel("", [])
                self.view.update_output_panel("")
                return

            exercise_num = int(choice)
            output = self.manager.run_exercise(block_name, exercise_num)
            self.view.update_output_panel(output)
