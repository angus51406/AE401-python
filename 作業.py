ms=float(input('請輸入數學考試成績'))
es=float(input('請輸入英文考試成績'))
if ((ms>90) and (es>90)):
    print('有獎')
elif((ms<60) and (es<60)):
    print('受罰')
elif((ms<60) or (es<60)):
    print('在加油')