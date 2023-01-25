#Ejercicio para crear un algoritmo para intercambiar variables introducidas por usuario

a = int (input ("a: "))
b = int (input ("b: "))

a, b = b, a


print(f"El valor de a es: {a}")

print(f"El valor de b es: {b}")