#exception handling
try:
    num=10
    deno=0
    
    result=num/deno
    
    print(result)
except:
    print('error:denominator cannot be 0')
    
    
    
try:
        even_numbers=[2,4,6,8]
        print(even_numbers[5])
        
except ZeroDivisionError:
    print('deno cannot be 0')

except IndexError:
    print('Index out of bound')
    
#assertion error 
try:
    num=int(input('enter a number:'))
    assert num % 2 == 0
except:
    print(' not a even number')
else:   #we can use else because we used assert keyword
    reciprocal=1/num
    print(reciprocal)
    
    
try:
    num=10
    deno=0
    
    result=num/deno
    
    print(result)
except:
    print('error:denominator cannot be 0')
finally:
    print('this is finally')