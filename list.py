scores=[]
n=int(input('請輸入班上有幾人'))
max=0
min=101
e=0
for i in range(n):
    s=int(input('請輸入每人分數'))
    scores.append(s)
    if s>max:
        max=s
    elif s<min:
        min=s
    e=e+s        
print('最高分數是',max,'最低分數是',min,'平均分數是',e/n)  