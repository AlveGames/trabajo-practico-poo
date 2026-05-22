class Block04:
    title = "Block 04 - Input / Output"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Read name and age, print greeting",
            "Exercise 2 - Read two numbers, print sum and average",
            "Exercise 3 - Read a number as string and concatenate '5'",
        ]

    def exercise_1(self):
        # 1. Ask for name and age, print a greeting
        nombre = input("¿Cuál es tu nombre? ")
        edad   = int(input("¿Cuántos años tienes? "))

        print(f"Hola, {nombre}! Tienes {edad} años.")

    def exercise_2(self):
        # 2. Read two numbers, compute sum and average
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))

        suma     = num1 + num2
        promedio = suma / 2

        print(f"Suma: {suma}")
        print(f"Promedio: {promedio}")

    def exercise_3(self):
        # 3. Read a number as string and concatenate "5" to show string vs int
        numero = input("Escribe un número: ")
        print(numero + "5")
