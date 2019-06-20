

# 88888888b                     oo oo                     dP                                 d8888b.     a8888a
#  88                                                      88                                     `88    d8' ..8b
# a88aaaa    88d8b.d8b. .d8888b. dP dP 88d888b. .d8888b. d8888P .d8888b. 88d888b.    dP   .dP .aaadP'    88 .P 88
#  88        88'`88'`88 88'  `88 88 88 88'  `88 88'  `88   88   88'  `88 88'  `88    88   d8' 88'        88 d' 88
#  88        88  88  88 88.  .88 88 88 88    88 88.  .88   88   88.  .88 88          88 .88'  88.     dP Y8'' .8P
#  88888888P dP  dP  dP `88888P' 88 dP dP    dP `88888P8   dP   `88888P' dP          8888P'   Y88888P 88  Y8888P
#                                88
#                                dP

# Sofware que te permete crear 56 diferentes emojis diferentes


import math

n = 51  # Proporcion

alto = n
ancho = n*2  #Creamos un grid con proporsion 1:2

Draw = [] # Lista con todas las cordenadas que serán coloreadas




#              ____ __ __ __  __   ___ __   ___   __  __  ____  __
#              ||    || || ||\ ||  //   ||  // \\  ||\ || ||    (( \
#              ||==  || || ||\\|| ((    || ((   )) ||\\|| ||==   \\
#              ||    \\_// || \||  \\__ ||  \\_//  || \|| ||___ \_))

def draw_triangulo(Pos_X,Pos_Y,lado):

    points = []
    for y in range (lado):
        for x in range(lado):
            if y == lado-1 or y//2 == (lado - 1)//2 - x or lado//2 + y//2 == x:
                points += [(x + Pos_X, y + Pos_Y,)]
    return points

def draw_flecha(Pos_X,Pos_Y,lado, direccion):

    points = []
    if direccion == 'up':
        for y in range (lado):
            for x in range(lado):
                if y//2 == (lado - 1)//2 - x or lado//2 + y//2 == x:
                    points += [(x + Pos_X, y + Pos_Y,)]
    if direccion == 'left':
        for y in range (lado):
            for x in range(lado):
                if x//2 == (lado - 1)//2 - y or lado//2 + x//2 == y:
                    points += [(x + Pos_X, y + Pos_Y,)]
    if direccion == 'right':
        for y in range(lado):
            for x in range(lado):
                if x // 2 == y or x // 2 == (lado - 1) - y:
                    points += [(x + Pos_X, y + Pos_Y,)]
    return points


def draw_circ(Pos_X,Pos_Y,radio):

    points = []
    for i in range(1000):
       points += [(int(math.sin(i) * radio) + Pos_X, int(math.cos(i) * radio) + Pos_Y)]
    return points


def draw_semiCirc(Pos_X,Pos_Y,r,curva, inverted):

    points = []
    if inverted == 0:
        for i in range(1000):
           points += [(int(math.sin(i) * r) + Pos_X, int(abs(math.cos(i)) * (r - curva) + Pos_Y))]
    if inverted == 1:
        for i in range(1000):
           points += [(int(math.sin(i) * r) + Pos_X, int(-abs(math.cos(i)) * (r - curva) + Pos_Y))]
    return points


def draw_rec(Pos_X, Pos_Y, largo, alto):

    points = []
    for y in range(alto):
        for x in range(largo):
            if x == 0 or x == largo - 1 or y == 0 or y == alto -1:
                points += [(x + Pos_X, y + Pos_Y)]

    return points




#             __ ___  ___ ____  __ __ ______  __
#             || ||\\//|| || \\ || || | || | (( \
#             || || \/ || ||_// || ||   ||    \\
#             || ||    || ||    \\_//   ||   \_))

pincel = input('Ingrese el caracter con el que quiere dibujar: ')

print()
print()
print('FORMA DE CARA:')
print()
print('[1]. Circular')
print('[2]. Rectangular')
print()

cara = int(input("Ingrese numero que desea: "))
while cara not in [1,2]:
    cara = int(input("Valor invalido, intente de nuevo: "))
print()

print('EXPRESIÓN:')
print()
print('[-3]. Extremadamente triste')
print('[-2]. Muy triste')
print('[-1]. triste')
print('[0]. Indiferente')
print('[1]. Feliz')
print('[2]. Muy Feliz')
print('[3]. Extremadamente feliz')
print()

sonrisa = int(input("Ingrese numero que desea: "))
while sonrisa not in range(-3,4):
    sonrisa = int(input("Valor invalido, intente de nuevo: "))
print()

print('FORMA DE OJOS:')
print()
print('[1]. circulares')
print('[2]. triangulares')
print('[3]. flechas hacia arriba')
print('[4]. flechas hacia adentro')
print()

ojos = int(input("Ingrese numero que desea: "))
while ojos not in range(1,5):
    ojos = int(input("Valor invalido, intente de nuevo: "))




#              ___      __   ___    __
#             // \\     ||  // \\  (( \
#            ((   ))    || ((   ))  \\
#             \\_//  |__||  \\_//  \_))
#
#  Diseño de ojos, el usuario podra escoger 2 tipos

if ojos == 1:
    Draw += draw_circ(ancho//2 - ancho//6, alto//2.5, 5)
    Draw += draw_circ(ancho//2 + ancho//6, alto//2.5, 5)
if ojos == 2:
    Draw += draw_triangulo(ancho//2 - ancho//5, alto//3, 10)
    Draw += draw_triangulo(ancho//2 + ancho//9, alto//3, 10)
if ojos == 3:
    Draw += draw_flecha(ancho//2 - ancho//5, alto//3, 9, 'up')
    Draw += draw_flecha(ancho//2 + ancho//9, alto//3, 9, 'up')
if ojos == 4:
    Draw += draw_flecha(ancho//2 - ancho//5, alto//3, 9, 'right')
    Draw += draw_flecha(ancho//2 + ancho//9, alto//3, 9, 'left')



#               ___  ___  ____   ____ ____  ___
#              //   // \\ || )) ||      // // \\
#             ((    ||=|| ||=)  ||==   //  ||=||
#              \\__ || || ||_)) ||___ //__ || ||
#
#  Diseño de cabeza, el usuario podra escoger 2 tipos disintos

if cara == 1:
    Draw += draw_circ(ancho//2,alto//2, 25)
if cara == 2:
    Draw += draw_rec(ancho//2-23, alto//2-18, 46, 36)

#               ____    ___     ___  ___
#               || ))  // \\   //   // \\
#               ||=)  ((   )) ((    ||=||
#               ||_))  \\_//   \\__ || ||
#
#  Diseño de boca, el usuario podra escoger 7 tipos distintos

if sonrisa == 3:
    Draw += draw_semiCirc(ancho//2, alto//2, 10, 0 , 0)
    Draw += draw_rec(ancho//2-10, alto//2, 20, 1)
if sonrisa == 2:
    Draw += draw_semiCirc(ancho//2, alto//2, 10, 0 , 0)
if sonrisa == 1:
    Draw += draw_semiCirc(ancho//2, alto//2, 10, 5 , 0)
if sonrisa == 0:
    Draw += draw_rec(ancho//2 - 5, alto//2, 10, 1 )
if sonrisa == -1:
    Draw += draw_semiCirc(ancho//2, alto//2, 10, 5 , 1)
if sonrisa == -2:
    Draw += draw_semiCirc(ancho//2, alto//2, 10, 0 , 1)
if sonrisa == -3:
    Draw += draw_semiCirc(ancho//2, alto//2, 10, 0 , 1)
    Draw += draw_rec(ancho//2-10, alto//2, 20,1)


for y in range(alto):
    for x in range(ancho):
        if (x,y) in Draw or x == 0 or y == 0 or x == ancho-1 or y == alto-1:
            print(pincel*2, end="")
        else:
            print("  ", end="")
    print()
