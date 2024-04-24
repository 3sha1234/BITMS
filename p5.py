def sum_numbers(numbers):
    return sum(num for num in numbers if num < 0), sum(num for num in numbers if num > 0 and num % 2 == 0), sum(num for num in numbers if num > 0 and num % 2 != 0)

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
sum_negative, sum_even_positive, sum_odd_positive = sum_numbers(numbers)
print("Sum of negative numbers:", sum_negative)
print("Sum of positive even numbers:", sum_even_positive)
print("Sum of positive odd numbers:", sum_odd_positive)
