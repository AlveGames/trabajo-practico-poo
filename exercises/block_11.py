class Block11:
    title = "Block 11 - Sets"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Union, intersection and difference of two sets",
            "Exercise 2 - Remove duplicates from a list using set",
            "Exercise 3 - Symmetric difference (A|B)-(A&B) vs A^B",
        ]

    def exercise_1(self):
        # 1. Create two sets and compute union, intersection and difference
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        print("Union:         ", A | B)
        print("Intersection:  ", A & B)
        print("Difference A-B:", A - B)
        print("Difference B-A:", B - A)

    def exercise_2(self):
        # 2. Remove duplicates from a list using set
        with_duplicates    = [1, 2, 2, 3, 3, 3, 4]
        without_duplicates = list(set(with_duplicates))
        print("Without duplicates:", without_duplicates)

    def exercise_3(self):
        # 3. Compute (A|B)-(A&B) and show it equals A^B (symmetric difference)
        A = {1, 2, 3}
        B = {3, 4, 5}
        result = (A | B) - (A & B)
        print("(A|B) - (A&B):", result)
        # Shorthand operator gives the same result
        print("Symmetric diff:", A ^ B)
        # Result is {1,2,4,5}: elements in A or B but not in both simultaneously
