email=["abc@gmail.com","dd@gmail.com","aaa@gmail.com"]
pwd=12345
emailid=str(input('enter emailid:'))
password=int(input('enter password:'))
if(email==emailid):
    if(pwd==password):
        print('login successful')
    else:
        print('login failed incorrect password')
else:
    print('login failed incorrect emailid')