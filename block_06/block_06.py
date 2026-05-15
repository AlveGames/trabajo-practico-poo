#1.-
contador = 1

while contador <= 10:
    print(contador)
    contador += 1


#2.-

frutas = ["manzana", "banana", "cereza", "mango", "uva"]

for indice, fruta in enumerate(frutas):
    print(f"{indice} - {fruta}")


#3.-

cuadrados_pares = [n ** 2 for n in range(1, 11) if n % 2 == 0]

print(cuadrados_pares)   
