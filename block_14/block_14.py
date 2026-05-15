def run():
#BLOCK 14 — Unpacking
    #Exercise 1 — Unpack (10, 20, 30, 40) → first, *middle, last
    # Unpacking the tuple into individual variables
    first, *middle, last = (10, 20, 30, 40)
    
    # Printing each variable to see the result
    print("first:", first)    # gets the first value
    print("middle:", middle)  # gets everything in between
    print("last:", last)      # gets the last value
    
    
    
    #Exercise 2 — Use *list to pass [2,3,4] as arguments to multiply(a,b,c)
    # Defining a function that multiplies three numbers
    def multiply(a, b, c):
        return a * b * c
    
    # Using * to unpack the list as individual arguments
    my_list = [2, 3, 4]
    result = multiply(*my_list)   # same as multiply(2, 3, 4)
    
    # Printing the final result
    print("result:", result)
    
    
    
    #Exercise 3 — Combine two dictionaries using ** without overwriting the originals
    
    # Defining two separate dictionaries
    dict1 = {"name": "Ana", "age": 25}
    dict2 = {"city": "Guayaquil", "country": "Ecuador"}
    
    # Combining both into a NEW dictionary using **
    # The originals are never modified
    combined = {**dict1, **dict2}
    
    # Printing the combined and the originals to verify
    print("combined:", combined)
    print("dict1 original:", dict1)   # still the same
    print("dict2 original:", dict2)   # still the same
