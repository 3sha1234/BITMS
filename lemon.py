n=int(input("enter a number of lemons:"))
print("equal" if n == 21 else "less by {}".format(21 - n ) if n < 21 else "more by {}".format(n - 21))