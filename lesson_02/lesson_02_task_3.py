import math

def square(side):
    x = side*side
    print(x)

side = input("Введите длину: ")

num_float = float(side)

num = math.ceil(num_float)

square(num)
