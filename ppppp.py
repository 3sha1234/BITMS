file_path='example.txt'
try:
    with open(file_path,'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('file not found')
    
except Exception as e:
    print('an error occurred:{e}')
finally:
    print('closing the file')