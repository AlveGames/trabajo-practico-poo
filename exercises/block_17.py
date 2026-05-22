import json


class Block17:
    title = "Block 17 - Mixins"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - AverageMixin: calculate student grade average",
            "Exercise 2 - ValidationMixin: validate email and age on registration",
            "Exercise 3 - ExportMixin: export sales report as JSON and CSV",
        ]

    def exercise_1(self):
        # 1. AverageMixin — calculate average grade for a student
        class AverageMixin:
            def calculate_average(self, grades):
                if not grades:
                    return 0
                for grade in grades:
                    if grade < 0 or grade > 20:
                        raise ValueError(f"La nota {grade} no es válida (debe estar entre 0 y 20)")
                return round(sum(grades) / len(grades), 2)

        class Student(AverageMixin):
            def __init__(self, name, grades):
                self.name   = name
                self.grades = grades

            def show_average(self):
                try:
                    average = self.calculate_average(self.grades)
                    print(f"\nEstudiante: {self.name}")
                    print(f"   Notas: {self.grades}")
                    print(f"   Promedio: {average}")
                except ValueError as error:
                    print(f"\nEstudiante: {self.name}")
                    print(f"   {error}")

        print("\n" + "=" * 50)
        print("EJERCICIO 1: PromedioMixin")
        print("=" * 50)
        Student("Daniel", [8,  9, 10]).show_average()
        Student("Ana",    [15, 16, 14]).show_average()

    def exercise_2(self):
        # 2. ValidationMixin — validate email and age before registering a user
        class ValidationMixin:
            def validate_email(self, email):
                if "@" not in email:
                    return False, "El email debe contener @"
                if not email.endswith(".com"):
                    return False, "El email debe terminar en .com"
                return True, "Email válido"

            def validate_age(self, age):
                if age < 18:
                    return False, f"Debe ser mayor de 18 años (edad actual: {age})"
                return True, "Edad válida"

        class User(ValidationMixin):
            def __init__(self, name, email, age):
                self.name  = name
                self.email = email
                self.age   = age

            def register(self):
                print(f"\nRegistrando usuario: {self.name}")
                email_valid, email_msg = self.validate_email(self.email)
                age_valid,   age_msg   = self.validate_age(self.age)
                print(f"   Email: {self.email} -> {email_msg}")
                print(f"   Edad:  {self.age}   -> {age_msg}")
                if email_valid and age_valid:
                    print(f"   Usuario '{self.name}' registrado correctamente")
                else:
                    print(f"   No se pudo registrar '{self.name}'")

        print("\n" + "=" * 50)
        print("EJERCICIO 2: ValidacionMixin")
        print("=" * 50)
        User("Ana",   "ana@email.com",   25).register()
        User("Pedro", "pedro@email.com", 16).register()
        User("Maria", "maria@gmail.com", 30).register()

    def exercise_3(self):
        # 3. ExportMixin — export a sales report in JSON and CSV formats
        class ExportMixin:
            def export_json(self, data):
                return json.dumps(data, indent=2, ensure_ascii=False)

            def export_csv(self, data):
                if not data:
                    return "No hay datos para exportar"
                columns = list(data[0].keys())
                csv = ",".join(columns) + "\n"
                for row in data:
                    csv += ",".join(str(row[col]) for col in columns) + "\n"
                return csv

        class Report(ExportMixin):
            def __init__(self, title, data):
                self.title = title
                self.data  = data

            def show_exports(self):
                print(f"\nREPORTE: {self.title}")
                print("-" * 40)
                print("\nFormato JSON:")
                print(self.export_json(self.data))
                print("\nFormato CSV:")
                print(self.export_csv(self.data))

        print("\n" + "=" * 50)
        print("EJERCICIO 3: ExportarMixin")
        print("=" * 50)
        sales = [
            {"product": "Laptop",   "quantity": 5,  "price": 800},
            {"product": "Mouse",    "quantity": 10, "price": 25},
            {"product": "Keyboard", "quantity": 3,  "price": 45},
        ]
        Report("Ventas 2024", sales).show_exports()
