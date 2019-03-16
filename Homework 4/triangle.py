def is_triangle_exist(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        is_exist = True
    else:
        is_exist = False
    return is_exist


def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            t_type = 'Equilateral triangle'
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            t_type = 'Isosceles triangle'
        else:
            t_type = 'Versatile triangle'
    else:
        t_type = 'Not a triangle'
    return t_type


if __name__ == "__main__":
    a = int(input('Input a: '))
    b = int(input('Input b: '))
    c = int(input('Input c: '))

    print(f'Is triangle possible: {is_triangle_exist(a, b, c)}')
    print(f'Type is: {triangle_type(a, b, c)}')


# Equilateral triangle (равносторонний)
# Isosceles triangle (равнобедренный)
# Versatile triangle (разносторонний)
# Not a triangle
