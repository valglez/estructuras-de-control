# Máquina de cálculo
# Es muy rudimentario y nada funcional 
# pero nos sirve para ejemplificar el uso de los condicionales

print('Vamos a multiplicar dos números')
print('  a. 5  b. 6  c. 3  ')
primera = input('Elige un número (a, b o c)')
if primera == 'a':
    print('  d. 7      e. 8 ')
    segunda = input('Elige un número (d o e)')
    if segunda == 'd':
        print('El resultado es 35')
    elif segunda == 'e':
        print('El resultado es 40')
if primera == 'b':
    print('  d. 7      e. 8 ')
    segunda = input('Elige un número (d o e)')
    if segunda == 'd':
        print('El resultado es 42')
    elif segunda == 'e':
        print('El resultado es 48')
if primera == 'c':
    print('  d. 7      e. 8 ')
    segunda = input('Elige un número (d o e)')
    if segunda == 'd':
        print('El resultado es 21')
    elif segunda == 'e':
        print('El resultado es 24')
else:
    print('Elección no disponible')




