edad = int(input('Escriba su edad: '))
if edad < 18:
    print('Usted es menor de edad')
    print('Usted aún no puede conducir un coche')
elif edad >= 18:
    print('Usted es mayor de edad')
    print('Usted si puede conducir un coche')
print(f'Usted tiene {edad} años')
