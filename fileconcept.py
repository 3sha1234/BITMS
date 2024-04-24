fileptr=open('trisha.txt','r')#opens the file 

if fileptr:
    print('file is opened successfully')
    
fileptr=open('trisha.txt','w')#writes the file
fileptr.write('harika')
print(fileptr)
fileptr.close

fileptr=open('trisha.txt','a')#append the file
fileptr.write('\nhi hello')
print(fileptr)
fileptr.close()

'''fileptr.read(2)
print(fileptr)
fileptr.close()'''