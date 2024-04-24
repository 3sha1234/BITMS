n={"a@gmail.com":"54","abd@gmail.com":"34521","abcd@gmail.com":"12131"}
otp=12345
e=str(input('enter emailid:'))
pas=int(input('enter password:'))
if e in n:
    if pas == n[e]:
        print('login successful')
        user_otp=int(input("enter otp:"))
        if user_otp==otp:
            print("logged into your account")
        else:
            print('invalid otp\n login failed')
            exit()
    else:
      print('password not found\n login failed')
      exit()  
else:
    print('login failed  emailid not found')
