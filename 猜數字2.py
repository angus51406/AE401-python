import random
big=int(input('請輸入最大上限'))
small=int(input('請輸入最小下限'))
n=random.randint(small,big)
chance=int(input('你想要有幾次機會'))
gs=0
for i in range(chance):
    gs=gs+1
    s=int(input('請輸入一個數字'))
    if s>big:
        print('輸入錯誤,請重新輸入')
        chance=chance+1
    elif s<small:
        print('輸入錯誤,請重新輸入')
        chance=chance+1
    elif s==n:
        print('答對了') 
        break
        
    elif s>n:
        print('小一點,你還剩',chance-gs,'次')
    elif s<n:
        print('大一點,你還剩',chance-gs,'次')
