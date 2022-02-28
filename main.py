from list_modificator import List
from game import game


def configuracion():
    while True:
        opt2 = input('''que te gustaria hacer?
        add
        read
        delete \n''')

        if opt2 == 'exit':
            break
        try:
            List.list_options[opt2.strip()]()
        except:
            print('ingresa un comando valido')


def jugar():

    game.eleccion()


if __name__ == '__main__':
    while True:
        opciones = {'jugar': jugar, 'configurar': configuracion}
        opt1 = input('''Que quieres hacer? 
    -jugar
    -configurar 
    -exit\n''')

        if opt1 == 'exit':
            break

        opciones[opt1.strip()]()


        print('ingresa un comando valido')
