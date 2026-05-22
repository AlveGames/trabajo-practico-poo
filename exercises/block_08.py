class Block08:
    title = "Block 08 - Lists"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - append() three elements, sort and print",
            "Exercise 2 - sum, max and min of [5,3,8,1,9,3]",
            "Exercise 3 - Shallow copy vs reference (alias) behaviour",
        ]

    def exercise_1(self):
        # 1. Create a list, append 3 elements with append(), sort and show it
        fruits = []
        fruits.append("apple")
        fruits.append("kiwi")
        fruits.append("banana")
        fruits.sort()
        print("Sorted list:", fruits)

    def exercise_2(self):
        # 2. Calculate sum, max and min of [5,3,8,1,9,3]
        numbers = [5, 3, 8, 1, 9, 3]
        print("Sum:  ", sum(numbers))
        print("Max:  ", max(numbers))
        print("Min:  ", min(numbers))

    def exercise_3(self):
        # 3. Show that copy=lista shares the same object; use .copy() for a real copy
        my_list = [1, 2, 3]
        copy    = my_list        # alias — same object
        copy.append(4)
        print("my_list:", my_list)   # also changed
        print("copy:   ", copy)

        # Correct form using .copy()
        my_list2  = [1, 2, 3]
        real_copy = my_list2.copy()
        real_copy.append(99)
        print("my_list2: ", my_list2)   # unchanged
        print("real_copy:", real_copy)
