num=int(input("Enter any number"))
try:
    l1=[1,2,3,4,5,6,7,8,9]
    print(1/num)
    index=int(input("enter index"))
    print("content: ", l1[index])
except Exception as e:
    print(e)
else:
    print("no Exception found")
finally:
    print("all files closed")