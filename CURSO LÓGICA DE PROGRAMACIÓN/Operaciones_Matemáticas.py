# Importar una Librería o Biblioteca de Funciones Matemáticas
import math

# ENTRADAS DE DATOS
# Declarar o crear Variables
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))

# PROCESOS (Cálculos u Operaciones Matemáticas y/o Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
# multiplicación =
# división = 
potencia1 = número_1 ** número_2
potencia2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada1 = math.sqrt(9)
raíz_cuadrada2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)
módulo_residuo = número_1 % número_2

# SALIDA DE DATOS
print("La suma es igual a", round(suma, 2))
print("La suma es igual a " + str(suma)) # CONCATENACIÓN (Unión de textos)
# CASTEO (Conversión de un tipo de dato en otro tipo de dato)
print(f"La suma es igual a {suma}")
print(f"El módulo o residuo de número1 y número2 es = {módulo_residuo}")
