def print_y_shape(name):
    length = len(name)
    for i in range(length):
        for j in range(length*2):
            if (j == i or j == (length*2-1-i)) and i <= length//2:
                print(name[i], end='')
            elif j == length and i > length//2:
                print(name[i], end='')
            else:
                print(' ', end='')
        print()

name = "Trisha"
print_y_shape(name)

