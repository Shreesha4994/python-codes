#Armstrong number
num=int(input())
num_str=str(num)
sum=0
for i in range(0,len(num_str)):
    sum+=int(num_str[i])**3
if(sum==num):
    print("Armstrong")
else:
    print("Not Armstrong")