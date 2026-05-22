class Block05:
    title = "Block 05 - Conditionals"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Even or odd check",
            "Exercise 2 - Grade classification (A-F)",
            "Exercise 3 - Login validation with username and password",
        ]

    def exercise_1(self):
        # 1. Check whether the input number is even or odd
        numero = int(input("Ingresa un número: "))

        if numero % 2 == 0:
            print(f"{numero} es PAR")
        else:
            print(f"{numero} es IMPAR")

    def exercise_2(self):
        # 2. Classify a grade (0-100) into a letter (A-F)
        nota = float(input("Ingresa la nota (0 - 100): "))

        if nota >= 90:
            letra = "A"
        elif nota >= 80:
            letra = "B"
        elif nota >= 70:
            letra = "C"
        elif nota >= 60:
            letra = "D"
        else:
            letra = "F"

        print(f"Tu calificación es: {letra}")

    def exercise_3(self):
        # 3. Validate a username/password combination
        usuario  = input("Usuario: ")
        password = input("Contraseña: ")

        if usuario == "admin" and password == "123":
            print("Bienvenido")
        else:
            print("Acceso denegado")
