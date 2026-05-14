#1 Crea dos conjuntos y calcula unión, intersección y diferencia.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:         ", A | B)  
print("Intersection:  ", A & B)   
print("Difference A-B:", A - B)   
print("Difference B-A:", B - A)

#2 Elimina los duplicados de [1,2,2,3,3,3,4] usando set.
with_duplicates = [1, 2, 2, 3, 3, 3, 4]
without_duplicates = list(set(with_duplicates))
print("Without duplicates:", without_duplicates)

#3 Calcula (A|B) - (A&B). Explica el resultado
A = {1, 2, 3}
B = {3, 4, 5}
result = (A | B) - (A & B)
print("(A|B) - (A&B):", result)          
# Shorthand operator:
print("Symmetric diff:", A ^ B) 
#The result is {1, 2, 4, 5} because these are the elements that belong to A or B, but not to both sets at the same time.