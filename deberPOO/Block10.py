#1 Crrea un dict de persona con nombre, edad y ciudad. Accede con [] y con get().
person = {
    "name":  "Ana",
    "age":   28,
    "city":  "Guayaquil"
}
print(person["name"])                  
print(person.get("age"))                 
print(person.get("phone", "N/A"))  

#2 Itera sobre los items del dict e imprime cada clave y valor.
for key, value in person.items():
    print(f"{key}: {value}")

#3 ¿Qué pasa si haces copia=datos y luego copia["b"]=2?
#The data also changes because both variables point to the same object.
data = {"a": 1, "b": 2}
ref = data              
ref["b"] = 99
print("data:", data) 

#Correct form:
data2 = {"a": 1, "b": 2}
real_copy2 = data2.copy()
real_copy2["b"] = 99
print("data2:     ", data2)   
print("real_copy2:", real_copy2)
