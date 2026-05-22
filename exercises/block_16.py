import json
import os


class Block16:
    title = "Block 16 - Files and JSON"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Write and read a plain text file",
            "Exercise 2 - Serialize and deserialize a simple dict to JSON",
            "Exercise 3 - Save and load a list of users as JSON",
        ]

    def exercise_1(self):
        # 1. Create a text file, write two lines and read them back
        if not os.path.exists("data"):
            os.makedirs("data")
            print("Carpeta 'data' creada")

        with open("data/file.txt", "w", encoding="utf-8") as file:
            file.write("Python\n")
            file.write("Segunda línea de ejemplo\n")

        print("Archivo 'data/file.txt' creado")

        with open("data/file.txt", "r", encoding="utf-8") as file:
            content = file.read()

        print("\nContenido del archivo:")
        print(content)

    def exercise_2(self):
        # 2. Dump a simple dict to JSON and load it back
        if not os.path.exists("data"):
            os.makedirs("data")

        data = {"x": 10, "y": 20}

        with open("data/data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        print("Archivo 'data/data.json' guardado")

        with open("data/data.json", "r", encoding="utf-8") as file:
            loaded = json.load(file)

        print(f"Datos cargados: {loaded}")

    def exercise_3(self):
        # 3. Write a list of user dicts to JSON and read them back
        if not os.path.exists("data"):
            os.makedirs("data")

        users = [
            {"name": "Ana",    "age": 20},
            {"name": "Luis",   "age": 30},
            {"name": "Carlos", "age": 25},
        ]

        with open("data/users.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=2)

        print("Archivo 'data/users.json' guardado")

        with open("data/users.json", "r", encoding="utf-8") as file:
            loaded = json.load(file)

        print("\nUsuarios cargados:")
        for user in loaded:
            print(f"  {user['name']} - {user['age']} años")
