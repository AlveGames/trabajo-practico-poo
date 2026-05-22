class Block06:
    title = "Block 06 - Loops"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - While loop: print 1 to 10",
            "Exercise 2 - For with enumerate over a fruit list",
            "Exercise 3 - List comprehension: even squares from 1 to 10",
        ]

    def exercise_1(self):
        # 1. Use a while loop to print 1 through 10
        contador = 1

        while contador <= 10:
            print(contador)
            contador += 1

    def exercise_2(self):
        # 2. Iterate a fruit list using enumerate
        frutas = ["manzana", "banana", "cereza", "mango", "uva"]

        for indice, fruta in enumerate(frutas):
            print(f"{indice} - {fruta}")

    def exercise_3(self):
        # 3. Build a list comprehension with squares of even numbers 1-10
        cuadrados_pares = [n ** 2 for n in range(1, 11) if n % 2 == 0]

        print(cuadrados_pares)
