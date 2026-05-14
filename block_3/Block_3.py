a = 20
b = 4

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Integer division: {a // b}")
print(f"Modulo: {a % b}")
print(f"Power: {a ** b}")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")

"""
x = 2 + 1 * 2 % 2 + (2**1)//2
1. (2**1) = 2
2. 1 * 2 = 2
3. 2 % 2 = 0
4. (2**1)//2 = 1
5. 2 + 0 + 1 = 3
Result: x = 3
"""
x = 2 + 1 * 2 % 2 + (2**1)//2
print(f"x = {x}")