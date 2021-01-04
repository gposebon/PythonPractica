while True:
    print('Who are you')
    nombre = input()
    if nombre != 'Joe':
        continue
    print('Hola Joe, cual es el password, (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Acceso permitido')