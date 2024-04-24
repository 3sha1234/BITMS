def print_v_shape(letter):
    for i in range(len(letter)):
        for j in range(len(letter)*2):
            if j == i or j == (len(letter)*2 - 1 - i):
                print(letter[i], end="")
            else:
                print(" ", end="")
        print()

name = "Trisha"
print_v_shape(name)