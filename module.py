import random
num=random.randint(1,10)
i=0
while i<1:
    n=float(input('請輸入1到10隨便一個數'))
    if n==num:
         print('你猜對了')    
         i=1
    elif n<num:
        print('太小了')
    elif n>num:
        print('太大了')
     
         
