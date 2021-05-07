#largest continue
maximum=int(0)
while(True):
    n=(input("enter num"))
    if(n!="done"):
        maximum=max(maximum,int(n))
        print("largest is",maximum)
    else:
        break