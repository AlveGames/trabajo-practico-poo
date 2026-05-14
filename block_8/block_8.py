#1 crear una lista, agrega 3 elementos con append(), ordénala y muéstrala.
fruits = []
fruits.append("apple")
fruits.append("kiwi")
fruits.append("banana")
fruits.sort()
print("Sorted list:", fruits)

#2 Calcula suma, máximo y mínimo de [5,3,8,1,9,3]
numbers = [5, 3, 8, 1, 9, 3]
print("Sum:  ", sum(numbers))   
print("Max:  ", max(numbers))   
print("Min:  ", min(numbers))

#3 ¿Qué pasa si haces copia=lista y luego copia.append(4)? ¿Por qué? 
#lista también cambia porque ambas variables apuntan al mismo objeto. 
my_list = [1, 2, 3]
copy = my_list          
copy.append(4)
print("my_list:", my_list)  
print("copy:   ", copy)   

#Correct form:
my_list2 = [1, 2, 3]
real_copy = my_list2.copy()
real_copy.append(99)
print("my_list2: ", my_list2)  
print("real_copy:", real_copy) 
