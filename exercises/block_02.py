class Block02:
    title = "Block 02 - Variables and Data Types"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Declare one variable of each simple and complex type",
            "Exercise 2 - List: first element, last element and slice [1:4]",
            "Exercise 3 - Class with str, list and dict attributes",
        ]

    def exercise_1(self):
        # 1. Declare one variable of each simple and complex type and print them
        myint    = 12
        myfloat  = 9.81
        mystring = "hi"
        mybool1  = True
        mybool2  = False

        print(myint)
        print(myfloat)
        print(mystring)
        print(mybool1)
        print(mybool2)

        mylist   = [12, 25, 30]
        mytupple = (11, "september", 2001)
        mydict   = {"name": "albert", "date": 12}
        print(mylist)
        print(mytupple)
        print(mydict)

    def exercise_2(self):
        # 2. Create a list with 5 elements; print first, last and list[1:4]
        print("____________________________")
        mylist1 = [11, 12, 31, 65, 34]

        print(mylist1[1:4])
        print(mylist1[0])
        print(mylist1[-1])

    def exercise_3(self):
        # 3. Class with str, list and dict attributes; print first char, last element, dict value
        print("________________________________________")

        class ant():
            def __init__(self, str2, list3, dict2):
                self.str   = str2
                self.list3 = list3
                self.dict2 = dict2

            def GreetList(self):
                print(f"first character of text is: {self.str[0]}")
                print(f"last item on the list is: {self.list3[-1]}")
                print(f"value of a dictionary key is: {self.dict2['name1']}")

        mylist3 = ant("valheim", [1, 2, 3], {"name1": "robert"})
        mylist3.GreetList()
