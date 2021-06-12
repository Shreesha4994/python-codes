#copy each line starting with vowel to another file
vowels=['A','a','E','e','i','o','u','I','O','U']
file = open("FROM.txt","r")
f = open("VOWELS.txt","a")
for line in file:
	if(line[0] in vowels):
		f.write(line)
		
