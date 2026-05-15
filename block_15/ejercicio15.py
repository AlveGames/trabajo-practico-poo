def run():
    
    # BLOCK 15: map, filter, reduce
    
    from functools import reduce
    
    def exercise1_map():
        numbers = [2, 4, 6]
        result = list(map(lambda x: x + 1, numbers))
        print(f"\n--- Ejercicio 1: map() ---")
        print(f"Lista original: {numbers}")
        print(f"Resultado (+1): {result}")
        return result
    
    def exercise2_filter():
        numbers = [1, 2, 3, 4, 5]
        result = list(filter(lambda x: x > 3, numbers))
        print(f"\n--- Ejercicio 2: filter() ---")
        print(f"Lista original: {numbers}")
        print(f"Números mayores a 3: {result}")
        return result
    
    def exercise3_reduce():
        numbers = [1, 2, 3, 4]
        result = reduce(lambda x, y: x * y, numbers)
        print(f"\n--- Ejercicio 3: reduce() ---")
        print(f"Lista original: {numbers}")
        print(f"Multiplicación de todos: {result}")
        return result
    
    def run_all():
        print("\n" + "="*50)
        print("BLOQUE 15 - map, filter, reduce")
        print("="*50)
        exercise1_map()
        exercise2_filter()
        exercise3_reduce()
    
    if __name__ == "__main__":
        run_all()
