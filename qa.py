def is_leap_year(year):
    n=int(input('enter the year:'))
    if ((n % 4 == 0 and n % 100 != 0) or n % 400 == 0):
        print("leap year")
        return true
        else:
            print('not leap year')
            return false
is_leap_year()
