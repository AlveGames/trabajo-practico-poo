# 📘 Guía Práctica Experimental 1 — POO en Python

## 🤖 IA utilizada
**Claude** — desarrollado por Anthropic  
**Deepseek** — bloques 15, 16 y 17

---

## 📁 Estructura del Proyecto

```
trabajo-practico-poo-main/
├── main.py
├── menu.py
├── block_0/Block_0.py
├── block_1/Block_1.py
├── block_2/Block_2.py
├── block_3/Block_3.py
├── block_8/block_8.py
├── block_9/block_9.py
├── block_10/block_10.py
├── block_11/block_11.py
├── block_12/block_12.py
├── block_13/block_13.py
├── block_14/block_14.py
├── block_15/ejercicio15.py
├── block_16/ejercicio16.py
└── block_17/ejercicio17.py
```

## 🚀 Cómo ejecutar
```bash
python main.py
```

---

## 📌 BLOQUE 0 — Introducción a la POO

**IA utilizada:** Claude

**Prompt para entender:** *"¿Qué es la POO y para qué sirven las clases en Python? ¿Puedo poner mis propias clases en vez de las del ejemplo?"*

**Prompt para proceso similar:** *"Dame un ejemplo de otro sistema distinto a una biblioteca y dime qué clases podría tener"*

**Mi resolución:** Identifiqué clases para un sistema de hospital: Paciente, Doctor, Cita, Farmacia, Historial. Luego practiqué creando una clase Animal con nombre y especie instanciando 3 objetos distintos.

**Repetición:** Lo repetí 2 veces hasta entender bien la diferencia entre clase e instancia.

---

## 📌 BLOQUE 1 — Constructor `__init__`

**IA utilizada:** Claude

**Prompt para entender:** *"¿Cómo hago una clase con __init__ y cómo agrego validación con raise ValueError? ¿Para qué sirve el @classmethod y qué es cls?"*

**Prompt para proceso similar:** *"Dame un ejemplo parecido con una clase Empleado con salario validado y un classmethod que lo cree desde un diccionario"*

**Mi resolución:** Creé la clase Employee con validación de salario negativo y un from_dictionary. Funcionó correctamente en ambas formas de instanciar.

**Repetición:** Lo repetí 2 veces. Al principio puse el @classmethod fuera de la clase y me daba error, después entendí que debe ir adentro con indentación.

---

## 📌 BLOQUE 2 — Variables y Tipos de Datos

**IA utilizada:** Claude

**Prompt para entender:** *"¿Cuáles son los tipos de datos simples y complejos en Python? ¿Por qué no puedo usar int, float o list como nombres de variables? ¿Cómo funciona el slicing lista[1:4]?"*

**Prompt para proceso similar:** *"Dame un ejercicio donde use todos los tipos de datos y acceda a posiciones específicas de una lista y un diccionario"*

**Mi resolución:** Practiqué con una clase DataBox que tenía una palabra, una lista de números y un diccionario de colores, accediendo al último carácter, primer número y una clave específica.

**Repetición:** Lo repetí 2 veces. Al principio usaba () para acceder a listas en vez de [], y también confundí la sintaxis del diccionario con corchetes.

---

## 📌 BLOQUE 3 — Operadores

**IA utilizada:** Claude

**Prompt para entender:** *"¿Cuáles son todos los operadores aritméticos en Python? ¿Cuál es la diferencia entre == e is? ¿Cómo se evalúa paso a paso una expresión con varios operadores?"*

**Prompt para proceso similar:** *"Dame una expresión con varios operadores para que yo explique el orden de evaluación paso a paso"*

**Mi resolución:** Practiqué con y = 3 + 2 ** 2 * 4 // 3 - 1 y lo resolví paso a paso. También probé == e is con tuplas para verificar la diferencia entre valor y referencia.

**Repetición:** Lo repetí 2 veces hasta entender bien la precedencia de operadores.

---

## 📌 BLOQUE 4 — Input / Output

IA utilizada: Claude
Prompt para entender: "¿Cómo funciona input() en Python y por qué siempre devuelve string? ¿Qué son las f-strings y cómo las uso para mostrar variables?"
Prompt para proceso similar: "Dame un ejercicio donde pida datos al usuario, los convierta al tipo correcto y los muestre con f-string"
Mi resolución: Practiqué solicitando nombre y edad con input(), convirtiendo la edad a int() y mostrando un mensaje personalizado con f-string. También calculé la suma y promedio de dos números ingresados, y verifiqué qué pasa cuando no se convierte el input al operar con strings.
Repetición: Lo repetí 2 veces. Al principio no entendía por qué "10" + "5" daba "105" en vez de 15; después quedó claro que sin int() el operador + concatena en lugar de sumar.

---

## 📌 BLOQUE 5 — Condicionales
IA utilizada: Claude
Prompt para entender: "¿Cómo funcionan if, elif y else en Python? ¿Cuándo uso and para combinar condiciones?"
Prompt para proceso similar: "Dame un ejercicio donde use if/elif/else para clasificar un valor y otro donde combine dos condiciones con and"
Mi resolución: Practiqué determinando si un número es par o impar con el operador módulo (%), asignando calificación letra (A, B, C, D, F) según rangos numéricos con elif encadenados, y creando un sistema de login que valida usuario y contraseña al mismo tiempo con and.
Repetición: Lo repetí 2 veces. La primera vez puse los rangos del elif en orden incorrecto y las notas altas caían en la rama equivocada; después entendí que el orden de las condiciones importa.

---

## 📌 BLOQUE 6 — Bucles
IA utilizada: Claude
Prompt para entender: "¿Cuál es la diferencia entre while y for en Python? ¿Para qué sirve enumerate() y cómo funciona una list comprehension?"
Prompt para proceso similar: "Dame un ejercicio donde use while con contador, otro con enumerate() sobre una lista y otro con list comprehension filtrando elementos"
Mi resolución: Imprimí los números del 1 al 10 con while usando un contador que incrementa con +=1. Recorrí una lista de frutas con enumerate() para obtener índice y valor al mismo tiempo. Generé la lista de cuadrados de números pares del 1 al 10 con list comprehension, obteniendo [4, 16, 36, 64, 100].
Repetición: Lo repetí 2 veces. La primera vez olvidé el contador += 1 dentro del while y el programa se quedó en bucle infinito; también confundí la sintaxis de la list comprehension hasta ver el orden correcto: [expresión for variable in iterable if condición].

---

## 📌 BLOQUE 7 — Funciones
IA utilizada: Claude
Prompt para entender: *"¿Cómo defino una función en Python con def y return? ¿Para qué sirve args y cómo funciona la recursividad?"
Prompt para proceso similar: *"Dame un ejercicio con una función simple, otro que acepte cantidad variable de argumentos con args y otro que use recursividad con un caso base"
Mi resolución: Creé la función doble(x) que retorna x * 2. Luego una función sumar(*args) que recorre todos los argumentos con un for y acumula el total, funcionando con cualquier cantidad de números. Finalmente implementé factorial(n) de forma recursiva, definiendo el caso base en n == 0 o n == 1 para detener las llamadas; verifiqué que factorial(5) retorna 120.
Repetición: Lo repetí 2 veces. La primera vez no puse el caso base en la función recursiva y el programa entró en recursión infinita; después entendí que toda función recursiva necesita una condición de parada.

---

## 📌 BLOQUE 8 — Listas

**IA utilizada:** Claude

**Prompt para entender:** *"¿Cómo uso append(), sort(), sum(), max() y min() en listas de Python? ¿Qué pasa si hago copia = lista y luego modifico la copia?"*

**Prompt para proceso similar:** *"Dame un ejercicio donde cree una lista vacía, agregue elementos, la ordene y demuestre la diferencia entre referencia y copia real"*

**Mi resolución:** Practiqué con una lista de números, calculé suma, máximo y mínimo, y verifiqué que al hacer copia = lista ambas cambian, pero con .copy() no.

**Repetición:** Lo repetí 2 veces hasta entender bien el concepto de referencia vs copia.

---

## 📌 BLOQUE 9 — Tuplas

**IA utilizada:** Claude

**Prompt para entender:** *"¿Por qué las tuplas son inmutables en Python? ¿Cómo funciona el unpacking con * en tuplas?"*

**Prompt para proceso similar:** *"Dame un ejercicio donde intente modificar una tupla y otro donde use unpacking para asignar valores"*

**Mi resolución:** Intenté modificar una tupla y capturé el TypeError con try/except. Practiqué unpacking con (100, 200, 300, 400) asignando a, b y *rest correctamente.

**Repetición:** Lo repetí 1 vez hasta entender bien el comportamiento inmutable.

---

## 📌 BLOQUE 10 — Diccionarios

**IA utilizada:** Claude

**Prompt para entender:** *"¿Cuál es la diferencia entre acceder a un diccionario con [] y con get()? ¿Qué pasa si modifico una copia de un diccionario?"*

**Prompt para proceso similar:** *"Dame un ejercicio donde cree un diccionario, lo recorra con items() y demuestre la diferencia entre referencia y copia"*

**Mi resolución:** Creé un diccionario de persona, lo recorrí con items() y verifiqué que ref = data modifica el original pero data.copy() no.

**Repetición:** Lo repetí 1 vez. Entendí que get() es más seguro porque no lanza error si la clave no existe.

---

## 📌 BLOQUE 11 — Conjuntos (set)

**IA utilizada:** Claude

**Prompt para entender:** *"¿Cómo funcionan las operaciones matemáticas con sets en Python? ¿Cómo elimino duplicados de una lista usando set?"*

**Prompt para proceso similar:** *"Dame un ejercicio donde calcule unión, intersección y diferencia entre dos conjuntos y explique la diferencia simétrica"*

**Mi resolución:** Practiqué con A = {1,2,3} y B = {3,4,5}, calculé todas las operaciones y verifiqué que (A|B) - (A&B) es equivalente a A^B.

**Repetición:** Lo repetí 1 vez hasta entender bien cada operación.

---

## 📌 BLOQUE 12 — Excepciones

**IA utilizada:** Claude

**Prompt para entender:** *"Explícame el bloque 12 de excepciones en Python. No entiendo qué hace el try/except cuando el usuario ingresa un valor incorrecto"*

**Prompt para proceso similar:** *"Hazme ejercicios similares al bloque 12 pero con programas diferentes para practicar try/except"*

**Mi resolución:** Practiqué capturando ValueError al convertir texto a número, IndexError al acceder a índices inexistentes, y manejé ambos errores en un mismo try/except.

**Repetición:** Lo repetí 3 veces. La primera vez no entendía cuándo usar cada tipo de error, pero después de probarlo con distintos inputs quedó claro.

---

## 📌 BLOQUE 13 — Decoradores

**IA utilizada:** Claude

**Prompt para entender:** *"Explícame qué es un decorador en Python y cómo funciona el @nombre_decorador antes de una función"*

**Prompt para proceso similar:** *"Hazme ejercicios similares al bloque 13 para practicar decoradores en Python"*

**Mi resolución:** Practiqué creando un decorador que valida si un número es par antes de procesarlo. Entendí que el wrapper es el que realmente se ejecuta.

**Repetición:** Lo repetí 3 veces. Las primeras veces no entendía bien el orden de ejecución, después quedó claro con el ejemplo de @log.

---

## 📌 BLOQUE 14 — Unpacking

**IA utilizada:** Claude

**Prompt para entender:** *"Explícame qué es el unpacking en Python y cómo funciona el operador * para desempaquetar valores"*

**Prompt para proceso similar:** *"Hazme ejercicios similares al bloque 14 para practicar unpacking en Python"*

**Mi resolución:** Practiqué desempaquetando tuplas con *middle, pasando listas como argumentos con * y combinando diccionarios con ** sin modificar los originales.

**Repetición:** Lo repetí 3 veces hasta entender la diferencia entre * para listas y ** para diccionarios.

---

## 📌 BLOQUE 15 — Funciones de Orden Superior

**IA utilizada:** Deepseek

**Prompt para entender:** *"Explícame map, filter y reduce en Python con ejemplos fáciles"*

**Prompt para proceso similar:** *"Genérame un ejercicio similar usando map para convertir grados Celsius a Fahrenheit"*

**Mi resolución:** Usé map con lambda para convertir temperaturas: celsius = [0, 10, 20, 30]. Funcionó correctamente.

**Repetición:** Lo repetí 2 veces. La primera vez confundí map con filter, pero después entendí que map transforma y filter filtra.

---

## 📌 BLOQUE 16 — Archivos y JSON

**IA utilizada:** Deepseek

**Prompt para entender:** *"Cómo guardar y leer archivos de texto y JSON en Python paso a paso"*

**Prompt para proceso similar:** *"Genérame un ejercicio para guardar una lista de contactos en JSON"*

**Mi resolución:** Creé contactos.json con nombre y teléfono, lo guardé con json.dump y lo leí con json.load correctamente.

**Repetición:** Lo repetí 1 vez. Al principio olvidaba encoding="utf-8" y los acentos salían mal.

---

## 📌 BLOQUE 17 — Mixins

**IA utilizada:** Deepseek

**Prompt para entender:** *"Qué son los Mixins en Python con ejemplos prácticos de POO"*

**Prompt para proceso similar:** *"Genérame un ejercicio similar para crear un Mixin que calcule áreas de figuras geométricas"*

**Mi resolución:** Creé un AreaMixin con métodos para calcular área de rectángulo y círculo, luego una clase Figura que lo hereda. Lo resolví entendiendo la lógica sin copiar.

**Repetición:** Lo repetí 3 veces. Las primeras 2 veces no entendía bien la herencia múltiple, después entendí que el Mixin es como una caja de herramientas que cualquier clase puede usar.

---

*Documentación generada como parte de la Guía Práctica Experimental 1 — POO en Python*
