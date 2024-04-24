def calculate(string):
    letters = 0
    digits = 0
    for char in string:
        if char.isalpha():
            letters+=1
        elif char.isdigit():
            digits+=1
    return letters,digits
a=input("enter a string:")
letters,digits = calculate(a)
print('number of letters:',letters)
print('number of digits:',digits)