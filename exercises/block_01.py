class Block01:
    title = "Block 01 - Constructor __init__"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Product class with code, name, price and negative-price validation",
            "Exercise 2 - Student class with default notes and classmethod from_dictionary",
        ]

    def exercise_1(self):
        # 1. Create Product class with code, name and price; instantiate 2 products
        # 2. Add validation so price cannot be negative
        class Product():
            def __init__(self, code, name, price):
                if price < 0:
                    raise ValueError("Error: the price cannot be negative")
                self.code  = code
                self.name  = name
                self.price = price

            def display(self):
                print(f"The product ID is: {self.code} ...with the name of: {self.name} ...at a price of: {self.price}")

        prod1 = Product("r1", "camera", 50)
        prod2 = Product("r2", "chair",  21)
        prod3 = Product("r3", "bed",   180)

        prod1.display()

    def exercise_2(self):
        # 3. Create Student with name and notes=None; if no notes start empty list
        # 4. Add @classmethod from_dictionary that creates a Student from a dict
        class Estudent():
            def __init__(self, name, notes=None):
                if notes is None:
                    self.notes = []
                else:
                    self.notes = notes
                self.name = name

            def display1(self):
                print(f"estudent: {self.name} note: {self.notes}")

            @classmethod
            def from_dictionary(cls, data):
                return cls(data["name"], data["notes"])

        est1 = Estudent("keni", [8, 9, 10])
        est1.display1()

        data = {"name": "caiza", "notes": [7, 8, 9]}
        est2 = Estudent.from_dictionary(data)
        est2.display1()
