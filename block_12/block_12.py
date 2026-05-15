def run():
    #BLOCK 12 — Exceptions (try / except)
    #Exercise 1 — Catch ValueError when converting user input to int
    # Asking the user to enter a whole number
    try:
        number = int(input("Enter a whole number: "))
        print("Number entered:", number)
    except ValueError as e:
        # Catching the error if the user types letters instead of a number
        print("Error: that is not a valid number.", e)
    
    
    
    
    #Exercise 2 — Catch IndexError when accessing list[5] in a 3-element list
    # Creating a list with only 3 elements (indexes 0, 1, 2)
    my_list = [10, 20, 30]
    
    try:
        # Trying to access an index that does not exist
        print(my_list[5])
    except IndexError as e:
        # Catching the error when the index is out of range
        print("Error: index out of range.", e)
    
    
    
    
    #Exercise 3 — Handle both ValueError and ZeroDivisionError
    try:
        # Asking the user for a number to divide 100
        number = int(input("Enter a number: "))
        result = 100 / number
        print("Result:", result)
    except ValueError as e:
        # Catching the error if the user types letters instead of a number
        print("Error: you must enter a valid number.", e)
    except ZeroDivisionError as e:
        # Catching the error if the user enters zero
        print("Error: cannot divide by zero.", e)
