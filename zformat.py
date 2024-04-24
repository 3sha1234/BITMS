def print_name_in_z_shape(name):
    n = len(name)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or i + j == n - 1:
                print(name[j], end=" ")
            else:
                print(" ", end=" ")
        print()

print_name_in_z_shape("TRISHA")