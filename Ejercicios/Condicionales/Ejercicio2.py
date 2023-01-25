'''
Pide 3 números y determine cuál es el mayor
'''

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if(n1 > n2 and n1 > n3):
    mayor = n1
elif(n2 > n1 and n2 > n3):
    mayor = n2
elif(n3 > n1 and n3 > n2):
    mayor = n3
elif(n1 == n2 and n2 == n3 and n1 == n3):
    print("Son iguales, no hay mayor")

print(f"El mayor es: {mayor}")
