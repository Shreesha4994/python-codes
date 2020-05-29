contin="yes"




	 


def menu() :	
		

		print("hi there ")
		print(contin)
		print("menu ")
		print("1. enter mail \n 2. search mail \n 3.display all mail")
		choice=int(input("enter the choice"))
		print(choice)

		

		if (choice==1):
			mail=input("enter the mail you want to store")
			if (val==1):
				f=open("emaildata.txt","a")
				f.write("\n")
				f.write(mail)
				f.close()
			continu()


		elif (choice==3):
			f=open("emaildata.txt","r")
			for line in f :
				print(line)
			f.close()
			continu()

		elif (choice==2):
			smail=input("enter the mail you want to search")
			f=open("emaildata.txt","r")
			
			for line in f :
				if(smail in line):
					found=1
			if (found==1):
				print("found!")
			else:
				print("not found")
			f.close()
			continu()
		

		else:
			print("invalid choice")
	

def continu() :
	contin=input("do you want to continue")
	print(contin)
	#main()
	if (contin=="yes"):
		menu()
	else:
		quit()




import re
regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check (email):
	if (re.search(regex,email)):
		print("valid mail")
		return 1;
	else:
		print("invalid")
		return 0;



menu()