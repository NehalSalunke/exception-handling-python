count=0
while count<5:
    try:
        num=int(input('Enter a number: '))
        if num<=2:
            raise ValueError('Please enter number>2')
        print('100 divided by',num,'is',100/num)
        break
    except ValueError as abc:
        print('error: ',abc)
        count+=1
    finally:
        print('you have exhausted the limit')


import xlrd
import datetime
import _datetime
