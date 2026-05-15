#1.-
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"{numero} es PAR")
else:
    print(f"{numero} es IMPAR")


#2.-

nota = float(input("Ingresa la nota (0 - 100): "))

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"  # Reprobado

print(f"Tu calificación es: {letra}")


#3.-

usuario  = input("Usuario: ")
password = input("Contraseña: ")

if usuario == "admin" and password == "123":
    print("Bienvenido")
else:
    print("Acceso denegado")
