edad = int(input('Escriba su edad: '))
if edad < 18:
    print('Usted es menor de edad')
    print('Usted aún no puede conducir un coche')
    miNombre = input('Dígame su nombre')
    print(f'{miNombre}, aún debe esperar ' f'{18 - edad} años para ser mayor de edad')
    print('Póngase en contacto con nosotros en un futuro')

elif edad >= 18:
    print('Usted es mayor de edad')
    print('Usted si puede conducir un coche')
    miNombre = input('Dígame su nombre')
    print(f'{miNombre} usted ya tiene ' f'{edad} años')
    print('Le voy a enviar un email para que pueda inscribirse en nuestra academia')
