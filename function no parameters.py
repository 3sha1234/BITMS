def harika():
    return 'this is my bank balance'
test_dict={'fname' : harika,'age' : 20, 'address' : 'ballari'}
print('the original dictionary is:' +str(test_dict))
res=test_dict['fname']()
print('the required call result:' +str(res))