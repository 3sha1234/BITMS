districts=set(['ooty','banglore','manglore','ballari','udupi'])
print("\nprinting the original set")
print(districts)
print("\nupdating the original set")
districts.discard('delhi')#no error
print('modified districts')
print(districts)

districts=set(['ooty','banglore','manglore','ballari','udupi'])
print("\nprinting the original set")
print(districts)
print("\nupdating the original set")
districts.remove('delhi')#shows error
print('modified districts')
print(districts)