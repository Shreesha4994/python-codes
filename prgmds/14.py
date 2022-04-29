fname = input("enter first name: ")
if(len(fname)<5):
    sname = input("Enter surname: ")
    print((fname+sname).upper())
else:
    print(fname.lower())