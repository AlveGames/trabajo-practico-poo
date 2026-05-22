class Block12:
    title = "Block 12 - Exceptions"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Catch ValueError when converting input to int",
            "Exercise 2 - Catch IndexError accessing list[5] in a 3-element list",
            "Exercise 3 - Handle both ValueError and ZeroDivisionError",
        ]

    def exercise_1(self):
        # 1. Catch ValueError when converting user input to int
        try:
            number = int(input("Enter a whole number: "))
            print("Number entered:", number)
        except ValueError as e:
            print("Error: that is not a valid number.", e)

    def exercise_2(self):
        # 2. Catch IndexError when accessing index 5 in a 3-element list
        my_list = [10, 20, 30]

        try:
            print(my_list[5])
        except IndexError as e:
            print("Error: index out of range.", e)

    def exercise_3(self):
        # 3. Handle both ValueError and ZeroDivisionError in one try block
        try:
            number = int(input("Enter a number: "))
            result = 100 / number
            print("Result:", result)
        except ValueError as e:
            print("Error: you must enter a valid number.", e)
        except ZeroDivisionError as e:
            print("Error: cannot divide by zero.", e)
