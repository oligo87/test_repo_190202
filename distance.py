def distance(x1, y1, x2, y2):
    '''
    Длинна отрезка А = √(X²+Y²) = √ ((X2-X1)²+(Y2-Y1)²).
    Принимает координаты точки в виде чисел, считает по формуле, возвращает длинну отрезка
    '''
    a = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return a


if __name__ == '__main__':
    x1 = int(input('Print the x1 point: '))
    y1 = int(input('Print the y1 point: '))
    x2 = int(input('Print hte x2 point: '))
    y2 = int(input('Print the y2 point: '))
    dist = distance(x1, y1, x2, y2)
    print(dist)