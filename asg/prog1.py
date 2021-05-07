#check grade
score=float(input("enter score"))
if score>1.0:
    grade="Error"
elif score>=0.9:
    grade='A'
elif score>=0.8:
    grade='B'
elif score >=0.7:
    grade='C'
elif score>=0.6:
    grade='D'
elif score>0.0:
    grade='F'
else:
    grade="Error"
print(grade)