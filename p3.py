dict1={1: 'harika',2: 'mahi',3: 'reshu'}
pop_key=dict1.pop(2)
print(dict1)
print()

#
emp={'name':'harika','age':20,'salary':1000000,'company':'infosys','dob':'2000-05-13'}
for x in emp:
    print(emp[x])
print()    

dict1={1: 'harika',2: 'mahi',3: 'reshu'}
print(sorted(dict1))
print('--------')


dict1={1: 'harika',2: 'mahi',3: 'reshu'}
dict1_demo=dict1.copy()
x=dict1_demo.pop(1)
print(x)
print(dict1_demo)


print(dict1.keys())
print(dict1.values())
dict1.update({1: 'vada'})
print(dict1)