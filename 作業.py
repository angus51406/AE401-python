ms=float(input('請輸入數學考試成績'))
es=float(input('請輸入英文考試成績'))
if ms and es >60:
    print('有獎')
elif ms and es <60:
    print('受罰')
elif ms or es >60:
    print('在加油')