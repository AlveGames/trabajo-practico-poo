import os
from model.block_manager import BlockManager
from view.console_view import ConsoleView
from controller.app_controller import AppController

if __name__ == "__main__":
    exercises_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exercises")
    AppController(
        manager=BlockManager(exercises_dir),
        view=ConsoleView(),
    ).run()
