class Block10:
    title = "Block 10 - Dictionaries"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Create person dict, access with [] and get()",
            "Exercise 2 - Iterate dict items printing each key and value",
            "Exercise 3 - Dict reference vs shallow copy",
        ]

    def exercise_1(self):
        # 1. Create a person dict and access values with [] and get()
        person = {
            "name": "Ana",
            "age":  28,
            "city": "Guayaquil",
        }
        print(person["name"])
        print(person.get("age"))
        print(person.get("phone", "N/A"))

    def exercise_2(self):
        # 2. Iterate over the dict items and print each key and value
        person = {
            "name": "Ana",
            "age":  28,
            "city": "Guayaquil",
        }
        for key, value in person.items():
            print(f"{key}: {value}")

    def exercise_3(self):
        # 3. Show that copy=data shares the same object; use .copy() for a real copy
        data = {"a": 1, "b": 2}
        ref  = data           # alias — same object
        ref["b"] = 99
        print("data:", data)  # also changed

        # Correct form using .copy()
        data2      = {"a": 1, "b": 2}
        real_copy2 = data2.copy()
        real_copy2["b"] = 99
        print("data2:     ", data2)       # unchanged
        print("real_copy2:", real_copy2)
