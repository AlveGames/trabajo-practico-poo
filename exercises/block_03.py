class Block03:
    title = "Block 03 - Operators"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - All arithmetic operators with a=20, b=4",
            "Exercise 2 - == vs is with two identical lists",
            "Exercise 3 - Operator precedence: x = 2 + 1*2%2 + (2**1)//2",
        ]

    def exercise_1(self):
        # 1. With a=20, b=4 print all arithmetic operators and their results
        a = 20
        b = 4

        print(f"Addition: {a + b}")
        print(f"Subtraction: {a - b}")
        print(f"Multiplication: {a * b}")
        print(f"Division: {a / b}")
        print(f"Integer division: {a // b}")
        print(f"Modulo: {a % b}")
        print(f"Power: {a ** b}")

    def exercise_2(self):
        # 2. Create two identical lists and show == is True but is is False
        print("--------------------------------------------------------------")
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = list1

        print(f"list1 == list2: {list1 == list2}")
        print(f"list1 is list2: {list1 is list2}")
        print(f"list1 is list3: {list1 is list3}")

    def exercise_3(self):
        # 3. Evaluate x = 2 + 1*2%2 + (2**1)//2 and explain precedence
        # 1. (2**1) = 2
        # 2. 1 * 2  = 2
        # 3. 2 % 2  = 0
        # 4. (2**1)//2 = 1
        # 5. 2 + 0 + 1 = 3   Result: x = 3
        print("--------------------------------------------------------------")
        x = 2 + 1 * 2 % 2 + (2**1)//2
        print(f"x = {x}")
