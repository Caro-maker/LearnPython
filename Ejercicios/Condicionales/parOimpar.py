'''
    Crear un programa en Python que
    pida 2 números y obtenga como resultado cual de ellos es par o si ambos lo son
'''

n1 = int (input("Número 1: "))
n2 = int (input ("Número 2: "))

if (n1%2 == 0 and n2%2 == 0):
   print("Ambos números son pares")
elif (n1%2 == 0 and n2%2 != 0):
    print(f"{n1} es par")
elif (n1%2 != 0 and n2%2 == 0):
    print(f"{n2} es par")
else:
    print("Son impares")
