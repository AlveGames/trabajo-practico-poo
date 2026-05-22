import os
import io
import sys
import importlib.util
from model.menu_model import Menu, Option


class BlockManager:
    """Scans exercises/ and exposes menus + exercise execution."""

    def __init__(self, exercises_dir: str):
        self.exercises_dir = exercises_dir
        self.blocks: dict = self._load_blocks()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _load_blocks(self) -> dict:
        """Import every block_XX.py and instantiate its BlockXX class."""
        blocks = {}
        for filename in sorted(os.listdir(self.exercises_dir)):
            if not (filename.startswith("block_") and filename.endswith(".py")):
                continue
            if filename == "__init__.py":
                continue

            module_name = filename[:-3]                          # block_00
            num_str = module_name.split("_")[1]                  # "00"
            class_name = f"Block{num_str}"                       # Block00

            filepath = os.path.join(self.exercises_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            block_class = getattr(module, class_name)
            blocks[module_name] = block_class()

        return blocks

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_main_menu(self) -> Menu:
        """Build the top-level menu listing every block."""
        options = [
            Option(label=block.title, value=name)
            for name, block in self.blocks.items()
        ]
        return Menu(title="GUÍA PRÁCTICA 1 - POO EN PYTHON", options=options)

    def get_block_menu(self, block_name: str) -> Menu:
        """Build the sub-menu listing every exercise inside a block."""
        block = self.blocks[block_name]
        options = [
            Option(label=desc, value=str(i))
            for i, desc in enumerate(block.exercises, 1)
        ]
        return Menu(title=block.title, options=options)

    def run_exercise(self, block_name: str, exercise_num: int) -> str:
        """Capture and return the exercise's stdout output."""
        block  = self.blocks[block_name]
        method = getattr(block, f"exercise_{exercise_num}")

        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            method()
        finally:
            output     = sys.stdout.getvalue()
            sys.stdout = old_stdout

        return output
