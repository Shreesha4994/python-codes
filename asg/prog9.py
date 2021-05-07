#sum of odd even
num=int(input("Enter num"))
sum_even=0
sum_odd=0
for i in range(num+1):
    if(i%2==0):
        sum_even+=i
    else:
        sum_odd+=i
print("Even sum:",sum_even)
print("Odd Sum:",sum_odd)