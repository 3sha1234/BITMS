def harika(a,b):
    print('this is my bank balance=',a+b)
test_dict={'fname' : harika,'age' : 20, 'address' : 'ballari'}
print('the original dictionary is:' +str(test_dict))
res=test_dict['fname'](10,20)
#print('the required call result:' +str(res))