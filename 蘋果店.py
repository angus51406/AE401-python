
sells={'num':0,
       'price':0,
       'sell':0}
persells=[]

q=0
i=0
x=0
t=0
while True:   
    print('這台機器有以下功能')
    print('1.設定')
    print('2.進貨')   
    print('3.出貨')
    print('4.營業額統計')
    print('5.庫存統計')
    print('6.退出系統')
    s=int(input('你要使用哪項功能'))
    if s==1:
        sells['num']=int(input('有幾顆蘋果'))
        m=int(input('一顆多少錢'))
        sells['price']=m
        print('目前有',sells['num'],'顆,一顆',m,'元')
    elif s==2:
        v=int(input('進多少個蘋果'))
        sells['num']=sells['num']+v
        print('目前有',sells['num'],'顆蘋果')    
    elif s==3:
       numout=int(input('輸入出貨數量:'))
       print('應付',numout*m,'元')
       sells['num']=sells['num']-numout
       sells['sell']=sells['sell']+numout
       temp_sells=[]
       temp_sells.append(numout)
       temp_sells.append(numout*m)
       persells.append(temp_sells)
       print('蘋果目前有',sells['num'],'顆')
    elif s==4:
        print('今天有',len(persells),'筆交易')
        for i in range(len(persells)):
            print('第',i+1,'次賣了',persells[i][0],'顆',persells[i][1],'元')
            print('共賣了',sells['sell'],'顆')
            print('營業額',sells['sell']*m,'元')
    elif s==5:
        print('蘋果目前有', sells['num'],'顆')
    elif s==6:
        t=str(sells['sell']*sells['price'])
        z='今日營業額是'+t+'元\n'
        r=str(sells['num'])
        y='剩下'+r+'顆'
        fo=open('黑心蘋果店.txt','w')
        fo.write(z)
        fo.write(y)
        break
    else:
        print('輸入錯誤,請重新輸入')