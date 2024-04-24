def find_largest_even_odd(numbers):
    largest_even = float('-inf')
    largest_odd = float('-inf')
    
    for num in numbers:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
        elif num % 2 != 0 and num > largest_odd:
            largest_odd = num
    
    return largest_even, largest_odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest_even, largest_odd = find_largest_even_odd(numbers)
print("Largest even number:", largest_even)
print("Largest odd number:", largest_odd)