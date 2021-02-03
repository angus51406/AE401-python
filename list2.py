scores=[]
n=int(input('請輸入班上有幾人'))
max=0
min=101

for i in range(n):
    
    s=str(input('請輸入姓名'))
    v=int(input('請輸入分數'))
    a=int(input('請輸入年齡'))
    if v>max:
       max=v
       maxnum=i
    if v<min:
       min=v
       minnum=i
    oneperson=list()   
    oneperson.append(s)
    oneperson.append(v)
    oneperson.append(a)
    scores.append(oneperson)
print('最高分:',max,'最低分:',min)
print('最高分的人:',scores[maxnum][0],scores[maxnum][2],'歲''最低分的人:',scores[minnum][0],scores[minnum][2],'歲')
