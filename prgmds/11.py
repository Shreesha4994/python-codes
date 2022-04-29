ans = input("Is it raining?")
ans.lower()
if(ans=="yes"):
    ans2 = input("is it windy?")
    if(ans2.lower()=="yes"):
        print("It is too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("Enjoy your day")