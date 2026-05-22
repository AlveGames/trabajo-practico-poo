class Block14:
    title = "Block 14 - Unpacking"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Unpack (10,20,30,40) -> first, *middle, last",
            "Exercise 2 - Use *list to pass [2,3,4] as args to multiply(a,b,c)",
            "Exercise 3 - Combine two dicts with ** without modifying originals",
        ]

    def exercise_1(self):
        # 1. Unpack the tuple into first, *middle, last
        first, *middle, last = (10, 20, 30, 40)

        print("first:", first)
        print("middle:", middle)
        print("last:", last)

    def exercise_2(self):
        # 2. Use * to unpack a list as positional arguments
        def multiply(a, b, c):
            return a * b * c

        my_list = [2, 3, 4]
        result  = multiply(*my_list)   # same as multiply(2, 3, 4)

        print("result:", result)

    def exercise_3(self):
        # 3. Combine two dicts using ** without modifying the originals
        dict1 = {"name": "Ana",       "age": 25}
        dict2 = {"city": "Guayaquil", "country": "Ecuador"}

        combined = {**dict1, **dict2}

        print("combined:", combined)
        print("dict1 original:", dict1)
        print("dict2 original:", dict2)
