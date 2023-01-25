#Obtener el radio y longitud de un circulo en python
import math 
'''formulas: 
    area = pi * radio al cuadrado
    longitud = 2 * pi *radio
'''

pi = math.pi
radio = float( input("radio: "))

area = pi * radio**2
longitud = 2*pi*radio

print(f"El area es: {area: .1f}") #Se le indica que se desea redondear un solo digito
print(f"La longitud es: {longitud: .1f}")
