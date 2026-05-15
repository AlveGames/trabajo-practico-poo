# BLOCK 16: Files and JSON

import json
import os

def exercise1_text_file():
    if not os.path.exists("data"):
        os.makedirs("data")
        print("📁 Carpeta 'data' creada")
    
    with open("data/file.txt", "w", encoding="utf-8") as file:
        file.write("Python\n")
        file.write("Segunda línea de ejemplo\n")
    
    print("✅ Archivo 'data/file.txt' creado")
    
    with open("data/file.txt", "r", encoding="utf-8") as file:
        content = file.read()
    
    print("\n📖 Contenido del archivo:")
    print(content)

def exercise2_simple_json():
    data = {"x": 10, "y": 20}
    
    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    
    print("✅ Archivo 'data/data.json' guardado")
    
    with open("data/data.json", "r", encoding="utf-8") as file:
        loaded = json.load(file)
    
    print(f"📖 Datos cargados: {loaded}")

def exercise3_users_list():
    users = [
        {"name": "Ana", "age": 20},
        {"name": "Luis", "age": 30},
        {"name": "Carlos", "age": 25}
    ]
    
    with open("data/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)
    
    print("✅ Archivo 'data/users.json' guardado")
    
    with open("data/users.json", "r", encoding="utf-8") as file:
        loaded = json.load(file)
    
    print("\n📖 Usuarios cargados:")
    for user in loaded:
        print(f"  👤 {user['name']} - {user['age']} años")

def run_all():
    print("\n" + "="*50)
    print("BLOQUE 16 - Archivos y JSON")
    print("="*50)
    exercise1_text_file()
    exercise2_simple_json()
    exercise3_users_list()
    print("\n✅ Bloque 16 completado")
    print("📁 Revisa la carpeta 'data' que se creó")

if __name__ == "__main__":
    run_all()