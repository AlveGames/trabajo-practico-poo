class Block09:
    title = "Block 09 - Tuples"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Tuple immutability: catch TypeError on assignment",
            "Exercise 2 - Unpacking (100,200,300,400) -> a, b, *rest",
            "Exercise 3 - Iterate list of coordinate tuples with for",
        ]

    def exercise_1(self):
        # 1. Create a tuple with 4 elements, try to modify the first and catch the error
        my_tuple = (10, 20, 30, 40)
        try:
            my_tuple[0] = 99
        except TypeError as e:
            print("Error:", e)

    def exercise_2(self):
        # 2. Use unpacking to assign (100, 200, 300, 400) -> a, b, *rest
        values = (100, 200, 300, 400)
        a, b, *rest = values
        print(f"a={a}, b={b}, rest={rest}")

    def exercise_3(self):
        # 3. Iterate a list of coordinate tuples and print x and y
        coordinates = [(1, 2), (3, 4), (5, 6)]
        for x, y in coordinates:
            print(f"x={x}, y={y}")
