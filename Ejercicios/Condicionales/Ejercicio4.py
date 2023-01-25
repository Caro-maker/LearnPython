'''
Crear un programa 
que simule un cajero automático
con un saldo inicial de 2000, 
con el siguiente menú:

1. Ingreso de dinero
2. Retirar dinero
3. Mostrar dinero
4. Salir
'''

saldoI = 2000.00
saldoMovimiento = 0.00
saldoTotal = 0.00
option = 0.00

print(f"Tienes = {saldoI}")
print("-----¿Qué deseas realizar?-----")
int(print("1. Ingreso de dinero"))
int(print("2. Retirar dinero"))
int(print("3. Mostrar dinero"))
int(print("4. Salir"))

if option == 1:
    saldoMovimiento = float(input("¿Cuánto deseas ingresar?: "))
    saldoTotal = saldoI + saldoMovimiento
elif option == 2:
    saldoMovimiento = print("¿Cuánto se desea retirar?")
    if saldoMovimiento < saldoTotal:
        saldoTotal = saldoI - saldoMovimiento
elif option == 3: 
    print(f"Tu saldo es:{saldoTotal}")
elif option == 4:

    