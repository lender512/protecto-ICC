import Draw

n = 50

height = n
width = n*2

PointList = []
print()
print('                 BIENVENIDO A DRAW®             ')
print()
print('Este software le permitira dinbujar libremente en un lienzo de 50x100 pixeles')
print('---------------------------------------------------------------------')
brush = input('Por favor ingrese el caracter con el que quiere dibujar: ')
print()
CantidadFiguras = int(input("Ingrese cantidad de figuras que desea dibujar: "))
print()
print()


for i in range(CantidadFiguras):
    print()
    print("Decida la figura que desea imprimir:")
    print()
    print("[1]. Linea")
    print('[2]. Triangulo')
    print('[3]. Rectangulo')
    print('[4]. Circulo')
    print('[5]. Semi circulo')
    print('[6]. Poligono')
    print()
    n = int(input("Ingrese número: "))
    while n not in range(1, 7):
        n = int(input("Valor invalido, Ingrese número de nuevo: "))

    if n == 1:
        pos_x1 = int(input("Ingrese la posicion eje x del primer punto: "))
        pos_y1 = int(input("Ingrese la posicion eje y del primer punto: "))
        pos_x2 = int(input("Ingrese la posicion eje x del segundo punto: "))
        pos_y2 = int(input("Ingrese la posicion eje y del segundo punto: "))

        PointList += Draw.line(pos_x1, pos_y1, pos_x2, pos_y2)

    if n == 2:
        pos_x = int(input("Ingrese la posicion eje x: "))
        pos_y = int(input("Ingrese la posicion eje y: "))
        lado = int(input("Ingrese el lado: "))

        PointList += Draw.triangle(pos_x, pos_y, lado)

    if n == 3:
        pos_x = int(input("Ingrese la posicion eje x: "))
        pos_y = int(input("Ingrese la posicion eje y: "))
        largo = int(input("Ingrese el largo: "))
        alto = int(input("Ingrese el alto: "))

        PointList += Draw.rec(pos_x, pos_y, largo, alto)

    if n == 4:
        pos_x = int(input("Ingrese la posicion eje x: "))
        pos_y = int(input("Ingrese la posicion eje y: "))
        radio = int(input("Ingrese el radio: "))

        PointList += Draw.circle(pos_x, pos_y, radio)

    if n == 5:
        pos_x = int(input("Ingrese la posicion eje x: "))
        pos_y = int(input("Ingrese la posicion eje y: "))
        radio = int(input("Ingrese el radio: "))
        curva = int(input("Ingrese el nivel de curva, (menor que el radio): "))
        inverted = int(input("Desea que este hacia [1] arriba o hacia [0] abajo: "))

        PointList += Draw.semicircle(pos_x, pos_y, radio, curva, inverted)

    if n == 6:
        lista = []
        cantidad = int(input('Ingrese los vertices que desee que tenga el poligono: '))
        for i in range(1, cantidad+1):
            pos_x = int(input("Ingrese la posicion eje x del punto " + str(i) + ": "))
            pos_y = int(input("Ingrese la posicion eje y del punto " + str(i) + ": "))
            lista.append(pos_x)
            lista.append(pos_y)
        cerrada = input('Desea que el poligono sea cerrado? [S/N]: ')
        while cerrada not in 'SN':
            n = int(input("Valor invalido, Ingrese de nuevo: "))
        if cerrada == 'S':
            PointList += Draw.poligono(lista, 1)
        elif cerrada == 'N':
            PointList += Draw.poligono(lista, 0)

for y in range(height):
    for x in range(width):
        if (x, y) in PointList or x == 0 or y == 0 or x == width-1 or y == height-1:
            print(brush*2, end="")
        else:
            print("  ", end="")
    print()

save = input('Desea guardar su dibujo? [S/N]')
if save == 'S':
    name = input('Ingrese el nombre con el que quiere guardar el archivo ("ejermplo.txt"): ')
    f = open(name, 'w+')
    for y in range(height):
        for x in range(width):
            if (x, y) in PointList or x == 0 or y == 0 or x == width - 1 or y == height - 1:
                f.write(brush * 2)
            else:
                f.write("  ")
        f.write("\n")
    print("Si el archivo ya existe, se sobrescribira.")
else:
    print("Gracias por usar el programa")
