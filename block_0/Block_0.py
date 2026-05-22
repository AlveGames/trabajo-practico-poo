def run():
    # 1. Identifica 5 clases para modelar un sistema de biblioteca. 
    # ✓ Posibles clases: Libro, Usuario, Prestamo, Autor, Categoria. 
    
    class Reader:
        pass
    
    class Author:
        pass
    
    class Editorial:
        pass
    
    class Program_Administrator:
        pass
    
    class Payment_System:
        pass
    
    # 2. Crea la clase Persona con nombre y edad. Instancia 3 objetos diferentes. 
    
    class Person:
        def __init__(self,Name, Age):
            self.Name = Name
            self.Age = Age
    
        def Greet(self):
            print(f"hi my name is {self.Name} and i´m {self.Age}")
    
    Person1 = Person("Joseph",21)
    Person2 = Person("Kain",12)
    Person3 = Person("Rose",18)
    
    Person3.Greet()
    
    # 3. Explica con tus palabras la diferencia entre clase y objeto. 
    """
    A class can be described as a blueprint or a template... whereas an object is
    basically "an instance," which we could interpret as if, after having
    the blueprint of a house (in this case, the class), the object would be the house already built...
    the main difference is that the class is only the design that exists in the code and
    doesn't occupy data space... while the object is the entity that already has its own
    and specific information... allowing many different houses to be created from a single template.
    """
"""a"""