def zellers_formula(day, month, year):
    
    d = year % 100
    c = year // 100
    
    day_of_week = (day + ((13 * (month + 1)) // 5) + d + (d // 4) + (c // 4) - (c*c)) % 7
    