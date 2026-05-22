from functools import reduce


class Block15:
    title = "Block 15 - Higher Order Functions"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - map(): add 1 to each element of [2,4,6]",
            "Exercise 2 - filter(): keep elements > 3 from [1,2,3,4,5]",
            "Exercise 3 - reduce(): multiply all elements of [1,2,3,4]",
        ]

    def exercise_1(self):
        # 1. Use map() to add 1 to each element
        numbers = [2, 4, 6]
        result  = list(map(lambda x: x + 1, numbers))
        print(f"\n--- Ejercicio 1: map() ---")
        print(f"Lista original: {numbers}")
        print(f"Resultado (+1): {result}")

    def exercise_2(self):
        # 2. Use filter() to keep only elements greater than 3
        numbers = [1, 2, 3, 4, 5]
        result  = list(filter(lambda x: x > 3, numbers))
        print(f"\n--- Ejercicio 2: filter() ---")
        print(f"Lista original: {numbers}")
        print(f"Números mayores a 3: {result}")

    def exercise_3(self):
        # 3. Use reduce() to multiply all elements together
        numbers = [1, 2, 3, 4]
        result  = reduce(lambda x, y: x * y, numbers)
        print(f"\n--- Ejercicio 3: reduce() ---")
        print(f"Lista original: {numbers}")
        print(f"Multiplicación de todos: {result}")
