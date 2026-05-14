#1 Crea una tupla con 4 elementos. Intenta modificar el primero y observa el error.
my_tuple = (10, 20, 30, 40)
try:
    my_tuple[0] = 99         
except TypeError as e:
    print("Error:", e)

#2 Usa unpacking para asignar los velores (100, 200, 300, 400) -> a, b,*resto.
values = (100, 200, 300, 400)
a, b, *rest = values
print(f"a={a}, b={b}, rest={rest}")

#3 Recorre una lista de coordenadas (tuplas) con for e imprime x e y.
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"x={x}, y={y}")
