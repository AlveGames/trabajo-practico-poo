def run():

    #Exercise 1 — Decorator that prints "Starting..." before executing the function
    # Decorator that prints a message before executing the original function
    def start(original_function):
        def wrapper(*args, **kwargs):
            print("Starting...")  # Message printed before the function runs
            result = original_function(*args, **kwargs)
            return result
        return wrapper
    
    # Applying the decorator to the greet function
    @start
    def greet():
        print("Hello! I am a decorated function.")
    
    # Calling the function
    greet()
    
    #Exercise 2 — Decorator that verifies the argument is positive before calculating its square
    # Decorator that checks if the number is positive before running the function
    def check_positive(original_function):
        def wrapper(n):
            if n <= 0:
                print("Error: the number must be positive.")
                return None
            return original_function(n)
        return wrapper
    
    # Applying the decorator to the square function
    @check_positive
    def square(n):
        print("The square is:", n ** 2)
    
    # Testing with a positive and a negative number
    square(4)    # works correctly
    square(-3)   # blocked by the decorator
    
    
    
    #Exercise 3 — Analyze: @log def suma(a,b). What does suma(2,3) print?
    
    # Decorator that logs when a function is called
    def log(original_function):
        def wrapper(*args, **kwargs):
            print("Calling function...")  # Printed before the function runs
            result = original_function(*args, **kwargs)
            return result
        return wrapper
    
    # Applying the decorator to the sum function
    @log
    def sum(a, b):
        return a + b
    
    # Calling the function and printing the result
    print(sum(2, 3))
    
    
    #Exercise 3 — Analyze: @log def suma(a,b). What does suma(2,3) print?

