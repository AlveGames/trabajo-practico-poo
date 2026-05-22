class Block00:
    title = "Block 00 - Introduction to OOP"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Identify 5 classes for a library system",
            "Exercise 2 - Create Person class and instantiate 3 objects",
            "Exercise 3 - Difference between class and object",
        ]

    def exercise_1(self):
        # 1. Identify 5 classes to model a library system
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

        print("Clases identificadas para el sistema de biblioteca:")
        for cls in [Reader, Author, Editorial, Program_Administrator, Payment_System]:
            print(f"  - {cls.__name__}")

    def exercise_2(self):
        # 2. Create Person class with name and age, instantiate 3 objects
        class Person:
            def __init__(self, Name, Age):
                self.Name = Name
                self.Age = Age

            def Greet(self):
                print(f"hi my name is {self.Name} and i´m {self.Age}")

        Person1 = Person("Joseph", 21)
        Person2 = Person("Kain", 12)
        Person3 = Person("Rose", 18)

        Person3.Greet()

    def exercise_3(self):
        # 3. Explain the difference between class and object
        print(
            "A class can be described as a blueprint or a template... whereas an object is\n"
            'basically "an instance," which we could interpret as if, after having\n'
            "the blueprint of a house (in this case, the class), the object would be the house already built...\n"
            "the main difference is that the class is only the design that exists in the code and\n"
            "doesn't occupy data space... while the object is the entity that already has its own\n"
            "and specific information... allowing many different houses to be created from a single template."
        )
