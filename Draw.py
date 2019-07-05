import math


def line(x_pos1, y_pos1, x_pos2, y_pos2):

    points = []  # Lista donde pondremos las coordenadas que seran pintadas.

    # Casos en los que la pendiente no sea infinita o 0
    if x_pos1-x_pos2 != 0 and y_pos1-y_pos2 != 0:
        pendiente = (y_pos2 - y_pos1)/(x_pos2 - x_pos1)

        # range() no acepta los valores cuando el start es mayor que el step
        if x_pos1 < x_pos2:
            for x in range(x_pos1, x_pos2 + 1):
                y = int(pendiente * x - pendiente * x_pos1 + y_pos1)
                points.append((x, y))
        if x_pos1 > x_pos2:
            for x in range(x_pos2, x_pos1 + 1):
                y = int(pendiente * x - pendiente * x_pos1 + y_pos1)
                points.append((x, y))

    # Casos en los que la pendiente es infinita
    elif x_pos1-x_pos2 == 0:

        # range() no acepta los valores cuando el start es mayor que el step
        if y_pos1 < y_pos2:
            for y in range(y_pos1, y_pos2+1):
                points.append((x_pos1, y))
        elif y_pos1 > y_pos2:
            for y in range(y_pos2, y_pos1+1):
                points.append((x_pos1, y))
    # Casos en los que la pendiente es 0
    elif y_pos1-y_pos2 == 0:

        # range() no acepta los valores cuando el start es mayor que el step
        if x_pos1 < x_pos2:
            for x in range(x_pos1, x_pos2+1):
                points.append((x, y_pos1))
        elif x_pos1 > x_pos2:
            for x in range(x_pos2, x_pos1+1):
                points.append((x, y_pos1))

    return points


def poligono(lista , cerrada):
    points = []
    if cerrada == 0:
        for i in range(0, len(lista)-3, 2):
            points += line(lista[i], lista[i+1], lista[i+2], lista[i+3])
    elif cerrada == 1:
        lista.append(lista[0])
        lista.append(lista[1])
        for i in range(0, len(lista)-3, 2):
            points += line(lista[i], lista[i+1], lista[i+2], lista[i+3])

    return points

def triangle(pos_x, pos_y, side):
    points = []
    altura = round((3 ** (1 / 3)) * (side // 2))
    cordenadaX_Altura = pos_x + side // 2
    cordenadaY_Altura = pos_y - altura

    points += poligono([pos_x, pos_y, cordenadaX_Altura, cordenadaY_Altura, pos_x + side, pos_y], 1)

    return points


def circle(pos_x, pos_y, radio):

    points = []
    for i in range(1000):
        points += [(int(math.sin(i) * radio) + pos_x, int(math.cos(i) * radio) + pos_y)]

    return points


def semicircle(pos_x, pos_y, r, curve, inverted):

    points = []
    if inverted == 0:
        for i in range(1000):
            points += [(int(math.sin(i) * r) + pos_x, int(abs(math.cos(i)) * (r - curve) + pos_y))]
    if inverted == 1:
        for i in range(1000):
            points += [(int(math.sin(i) * r) + pos_x, int(-abs(math.cos(i)) * (r - curve) + pos_y))]

    return points


def rec(pos_x, pos_y, largo, alto):

    points = []
    points += poligono([pos_x, pos_y, pos_x + largo, pos_y, pos_x + largo, pos_y + alto, pos_x, pos_y + alto], 1)

    return points
