class Block07:
    title = "Block 07 - Functions"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Function doble(x) returning x*2",
            "Exercise 2 - Function sumar(*args) with variable arguments",
            "Exercise 3 - Recursive factorial(n)",
        ]

    def exercise_1(self):
        # 1. Define and call doble(x)
        def doble(x):
            return x * 2

        print(doble(5))
        print(doble(3.5))

    def exercise_2(self):
        # 2. Define sumar with *args to accept any number of arguments
        def sumar(*args):
            total = 0
            for numero in args:
                total += numero
            return total

        print(sumar(1, 2, 3))
        print(sumar(10, 20, 30, 40))
        print(sumar(5))

    def exercise_3(self):
        # 3. Recursive factorial
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)

        print(factorial(5))
        print(factorial(0))
        print(factorial(7))
