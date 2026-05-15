def run():
    # BLOCK 17: Mixins
    
    import json
    
    # MIXIN 1: AverageMixin
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
            self.name = name
            self.grades = grades
        
        def show_average(self):
            try:
                average = self.calculate_average(self.grades)
                print(f"\n📚 Estudiante: {self.name}")
                print(f"   📝 Notas: {self.grades}")
                print(f"   🎯 Promedio: {average}")
                return average
            except ValueError as error:
                print(f"\n📚 Estudiante: {self.name}")
                print(f"   ❌ {error}")
                return None
    
    # MIXIN 2: ValidationMixin
    class ValidationMixin:
        def validate_email(self, email):
            if "@" not in email:
                return False, "❌ El email debe contener @"
            if not email.endswith(".com"):
                return False, "❌ El email debe terminar en .com"
            return True, "✅ Email válido"
        
        def validate_age(self, age):
            if age < 18:
                return False, f"❌ Debe ser mayor de 18 años (edad actual: {age})"
            return True, "✅ Edad válida"
    
    class User(ValidationMixin):
        def __init__(self, name, email, age):
            self.name = name
            self.email = email
            self.age = age
        
        def register(self):
            print(f"\n👤 Registrando usuario: {self.name}")
            email_valid, email_msg = self.validate_email(self.email)
            age_valid, age_msg = self.validate_age(self.age)
            print(f"   📧 Email: {self.email} -> {email_msg}")
            print(f"   🎂 Edad: {self.age} -> {age_msg}")
            
            if email_valid and age_valid:
                print(f"   ✅ Usuario '{self.name}' registrado correctamente")
                return True
            else:
                print(f"   ❌ No se pudo registrar '{self.name}'")
                return False
    
    # MIXIN 3: ExportMixin
    class ExportMixin:
        def export_json(self, data):
            return json.dumps(data, indent=2, ensure_ascii=False)
        
        def export_csv(self, data):
            if not data:
                return "No hay datos para exportar"
            columns = list(data[0].keys())
            csv = ",".join(columns) + "\n"
            for row in data:
                values = [str(row[col]) for col in columns]
                csv += ",".join(values) + "\n"
            return csv
    
    class Report(ExportMixin):
        def __init__(self, title, data):
            self.title = title
            self.data = data
        
        def show_exports(self):
            print(f"\n📊 REPORTE: {self.title}")
            print("-" * 40)
            print("\n📄 Formato JSON:")
            print(self.export_json(self.data))
            print("\n📄 Formato CSV:")
            print(self.export_csv(self.data))
    
    def exercise1_average():
        print("\n" + "="*50)
        print("EJERCICIO 1: PromedioMixin")
        print("="*50)
        
        student1 = Student("Daniel", [8, 9, 10])
        student1.show_average()
        
        student2 = Student("Ana", [15, 16, 14])
        student2.show_average()
    
    def exercise2_validation():
        print("\n" + "="*50)
        print("EJERCICIO 2: ValidacionMixin")
        print("="*50)
        
        user1 = User("Ana", "ana@email.com", 25)
        user1.register()
        
        user2 = User("Pedro", "pedro@email.com", 16)
        user2.register()
        
        user3 = User("Maria", "maria@gmail.com", 30)
        user3.register()
    
    def exercise3_export():
        print("\n" + "="*50)
        print("EJERCICIO 3: ExportarMixin")
        print("="*50)
        
        sales = [
            {"product": "Laptop", "quantity": 5, "price": 800},
            {"product": "Mouse", "quantity": 10, "price": 25},
            {"product": "Keyboard", "quantity": 3, "price": 45}
        ]
        
        report = Report("Ventas 2024", sales)
        report.show_exports()
    
    def run_all():
        print("\n" + "█"*50)
        print("        BLOQUE 17 - MIXINS")
        print("█"*50)
        exercise1_average()
        exercise2_validation()
        exercise3_export()
        print("\n" + "="*50)
        print("✅ Bloque 17 completado")
        print("="*50)
    
    if __name__ == "__main__":
        run_all()
