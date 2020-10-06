#Usamos los condicionales para mezclar colores

print('Este programa mezcla dos colores.')
print('  r. Rojo      a. Azul')
primera = input('  Elija un color (r o a): ')
if primera == 'r':
    print('  am. Amarillo      v. Verde')
    segunda = input('  Elija un color (am o v): ')
    if segunda == 'am':
        print('La mezcla de Rojo y Amarillo produce Naranja')
    elif segunda == 'v':
        print('La mezcla de Rojo y Verde produce Marrón')
if primera == 'a':
    print('  am. Amarillo     v. Verde')
    segunda = input('  Elije un color (am o v): ')
    if segunda == 'am':
        print('La mezcla de Azul y Amarillo produce Verde')
    elif segunda == 'v':
        print('La mezcla de Azul y Verde produce Turquesa')
        