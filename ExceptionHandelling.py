num= int(input("Enter a number: "))
try:
    print("hello")
    l1=[1,2,3,4,5,6]
    index=int(input("Enter any index: "))
    print(l1[index])
    print("indexing done")
    print(1/num)
    print("division done without exception")

except Exception as nehal:
    print(nehal)