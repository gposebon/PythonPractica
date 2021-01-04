import sys

while True:
    print('Escriba exit para salir')
    respuesta = input()
    if respuesta == 'exit':
        sys.exit()
    print('Usted escribio ' + respuesta)