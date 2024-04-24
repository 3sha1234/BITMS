email="abc@gmail.com"
pwd=12345
emailid=str(input('enter emailid:'))
password=int(input('enter password:'))
if(email==emailid and pwd==password):
    print('login successful')
else:
    print('login failed')