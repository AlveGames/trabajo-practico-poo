from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Option:
    label: str
    value: str


@dataclass
class Menu:
    title: str
    options: List[Option] = field(default_factory=list)

    def is_valid_choice(self, raw: str) -> bool:
        """Return True for '0' (back/exit) or any valid 1-based index."""
        if raw == "0":
            return True
        try:
            idx = int(raw)
            return 1 <= idx <= len(self.options)
        except ValueError:
            return False

    def get_option(self, raw: str) -> Option:
        """Return the Option for a 1-based numeric string."""
        return self.options[int(raw) - 1]
