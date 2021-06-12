#copy each line starting with vowel to another file
vowels=['A','a','E','e','i','o','u','I','O','U']
file = open("sample3.txt","r")
f = open("vowels.txt","a")
for line in file:
	if(line[0] in vowels):
		f.write(line)
		