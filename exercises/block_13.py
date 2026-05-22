class Block13:
    title = "Block 13 - Decorators"

    def __init__(self):
        self.exercises = [
            "Exercise 1 - Decorator that prints 'Starting...' before the function",
            "Exercise 2 - Decorator that verifies argument is positive before squaring",
            "Exercise 3 - @log decorator: what does suma(2,3) print?",
        ]

    def exercise_1(self):
        # 1. Decorator that prints "Starting..." before executing the function
        def start(original_function):
            def wrapper(*args, **kwargs):
                print("Starting...")
                result = original_function(*args, **kwargs)
                return result
            return wrapper

        @start
        def greet():
            print("Hello! I am a decorated function.")

        greet()

    def exercise_2(self):
        # 2. Decorator that checks the argument is positive before squaring it
        def check_positive(original_function):
            def wrapper(n):
                if n <= 0:
                    print("Error: the number must be positive.")
                    return None
                return original_function(n)
            return wrapper

        @check_positive
        def square(n):
            print("The square is:", n ** 2)

        square(4)    # works correctly
        square(-3)   # blocked by the decorator

    def exercise_3(self):
        # 3. @log decorator: analyse what suma(2,3) prints
        def log(original_function):
            def wrapper(*args, **kwargs):
                print("Calling function...")
                result = original_function(*args, **kwargs)
                return result
            return wrapper

        @log
        def sum(a, b):
            return a + b

        print(sum(2, 3))
