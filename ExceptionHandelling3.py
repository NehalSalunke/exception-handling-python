try:
    num = int(input("enter any number"))
    l1=[1,2,3,4,5,6]
    print(3/num)
    import abcd
    print(l1[5])
    import csv
    infile=open(r'./../Data/newemp1.csv','r')
    abc=csv.reader(infile)
    for each in abc:
        print(each)
except IndexError as E:
    print("i am in index error b;ock")
except ImportError as IE:
    print("i am in import error block")
except ZeroDivisionError as ZD:
    print("i am in zero division error")
except FileNotFoundError as fnf:
    print("file not found")
except Exception as General:
    print("general Exception")
else:
    print("No exception occured")
finally:
    print("all files are closed")