emp={'name':'harika','age':20,'salary':1000000,'company':'infosys','dob':'2000-05-13'}
print(type(emp))
print('printing employee data...')
print(emp)
print('deleting some of the employee data')
del emp['name']
del emp['company']
print('printing the modified information')
print(emp)
print('deleting dictionary')
del emp
print('lets try to print it again')
print(emp)