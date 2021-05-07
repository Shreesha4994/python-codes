#Leap Year
year=int(input("Enter year"))
if(year%4==0 and year%100!=0):
    res='Leap'
elif(year%100==0):
    res='Not Leap'
elif(year%400==0):
    res='Leap'
else:
    res='Not Leap'
print(res)