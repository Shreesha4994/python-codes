#series sum
def series1(num):
    sum=int(0)
    for i in range(1,num+1):
        sum+=(1/i)
    return sum

def series2(num):
    sum=int(0)
    for i in range(1,num+1):
        sum+=((i**i)/i)
    return sum
num=int(input("Enter num"))
print(series1(num))
print(series2(num))