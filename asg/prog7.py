#fibonacci
def fib(num):
    first=0
    second=1
    count=0
    if(num<=0):
        print("Invalid Input")
    if(num==1):
        print(first)
    else:
       while(count<num):
           print(first)
           third=first+second
           first=second
           second=third
           count+=1
num=int(input("Enter number"))
fib(num)