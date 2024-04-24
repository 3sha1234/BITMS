for rn in range(1,101):
    if rn>50:
        break#skips bunch of values
    else:
        print('alllowed', rn)
        
for rn in range(1,101):
    if rn==25 or rn==50 or rn==75:
        continue#skips specified values
    else:
        print('alllowed', rn)