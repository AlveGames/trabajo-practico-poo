import sys
import os

# Add each block folder to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_0"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_1"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_2"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_3"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_8"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_9"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_10"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_11"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_12"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_13"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_14"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_15"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_16"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "block_17"))

import Block_0
import Block_1
import Block_2
import Block_3
import block_8
import block_9
import block_10
import block_11
import block_12
import block_13
import block_14
import ejercicio15
import ejercicio16
import ejercicio17

from menu import Menu


# Blocks not yet implemented
def not_available():
    print("\n  # Block not yet available (TODO)\n")


options = {
    "1":  ("Block 0  - Introduction to OOP",        Block_0.run),
    "2":  ("Block 1  - Constructor __init__",        Block_1.run),
    "3":  ("Block 2  - Variables and Data Types",    Block_2.run),
    "4":  ("Block 3  - Operators",                   Block_3.run),
    "5":  ("Block 4  - Input / Output",              not_available),
    "6":  ("Block 5  - Conditionals",                not_available),
    "7":  ("Block 6  - Loops",                       not_available),
    "8":  ("Block 7  - Functions",                   not_available),
    "9":  ("Block 8  - Lists",                       block_8.run),
    "10": ("Block 9  - Tuples",                      block_9.run),
    "11": ("Block 10 - Dictionaries",                block_10.run),
    "12": ("Block 11 - Sets",                        block_11.run),
    "13": ("Block 12 - Exceptions",                  block_12.run),
    "14": ("Block 13 - Decorators",                  block_13.run),
    "15": ("Block 14 - Unpacking",                   block_14.run),
    "16": ("Block 15 - Higher Order Functions",      ejercicio15.run),
    "17": ("Block 16 - Files and JSON",              ejercicio16.run),
    "18": ("Block 17 - Mixins",                      ejercicio17.run),
}

if __name__ == "__main__":
    main_menu = Menu("PRACTICAL GUIDE 1 - OOP IN PYTHON", options)
    main_menu.run()
