'''Crea un programa que compare dos nombres,
 y verificar si hay coincidencia o no,
  si es que ambos nombres comienzan con la misma letra 
  o si terminan con la misma letra.
'''

nombre1 = input("Nombre 1: ")
nombre2 = input("Nombre 2: ")

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencia")
else:
    print("No hay coincidencia\n Entre la primera y la última")
