def print_name_in_x_shape(name):
    n=len(name)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n -1:
                print(name[i],end=" ")
            else:
                    print(" ",end=" ")
        print()
        
print_name_in_x_shape("TRISHA")