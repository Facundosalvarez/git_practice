# Write your code here
# para generar selecciones de la computadora aleatoriamente
import random

name = input('Enter your name: ')

print('Hello, ' + name)
# generar las reglas de juego se ingresan las opciones que se pueden elegir
options = ['rock', 'paper', 'scissors']
in2 = input()
if in2 == "":
    options = ['rock', 'paper', 'scissors']
else:
    options = in2.split(',')
print('Okay, let\'s start')

# las opciones partidas a la mitad si se escoge de una mitad se gana a la otra mitad si se escoge el mismo es empate

# abre el archivo donde estan almacenados los puntajes
file_open = open('rating.txt', 'r')
# lee la lista de nombres y la separa en una lista
list_names = file_open.readlines()
score = 0
# busca en la lista de nombres si se encuentra el nombre ingresado
for i in range(len(list_names)):
    if name in list_names[i]:
        score = int(list_names[i].strip('\n').split(' ')[1])
    else:
        continue


# se empieza el juego y se escoge una opcion para jugar


def winoptions(in1, lista):
    mitad_de_len_lista = int(len(lista) / 2)

    index_in1_en_lista = lista.index(in1) + 1

    len_desde_seleccion_hasta_fin = len(lista[index_in1_en_lista:])

    faltante_de_lista = mitad_de_len_lista - len_desde_seleccion_hasta_fin
    if faltante_de_lista < 0:

        return lista[index_in1_en_lista:index_in1_en_lista + mitad_de_len_lista]
    else:

        return lista[index_in1_en_lista:] + lista[:faltante_de_lista]


def loseoptions(in1, lista):
    mitad_de_len_lista = int(len(lista) / 2)  # 2

    index_in1_en_lista = lista.index(in1)  # b = 1

    len_hasta_in1 = index_in1_en_lista  # 1

    faltante_de_lista = len_hasta_in1 - mitad_de_len_lista  # -1
    if faltante_de_lista >= 0:

        return lista[index_in1_en_lista - mitad_de_len_lista:index_in1_en_lista]
    else:
        return lista[(faltante_de_lista):] + lista[:index_in1_en_lista]


# se empieza el juego y se escoge una opcion para jugar

# se genera la opcion al azar de la computadora
while True:
    in1 = input().lower()
    computer = random.choice(options)

    if in1 == computer:
        print('There is a draw ({})'.format(in1))
        score += 50
    elif in1 == '!rating':
        print('Your rating: ' + str(score))
    elif in1 == '!exit':
        print('Bye!')
        exit()
    elif in1 not in list(options):
        print('Invalid input')
        continue

    elif computer in loseoptions(in1, options):
        print('Well done. The computer chose {} and failed'.format(computer))
        score += 100


    elif computer in winoptions(in1, options):
        print('Sorry, but the computer chose {}'.format(computer))




