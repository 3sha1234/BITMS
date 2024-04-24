def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

user_input = input("Enter five values separated by commas: ")
values = [int(x) for x in user_input.split(",")]

prime_values = [value for value in values if is_prime(value)]
leap_years = [year for year in values if is_leap_year(year)]

print("Prime values:", prime_values)
print("Leap years:", leap_years)
