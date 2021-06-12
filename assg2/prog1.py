#count no of vowels,words,a-count,text-count,space-count
vowels=['A','a','E','e','i','o','u','I','O','U']
word_count=v_count=text_count=a_count=space_count=int(0)
file = open("textfile.txt","r")
for line in file:
	space_count+=line.count(" ")
	a_count+=line.count("a")
	text_count+=line.count("Text ")
	text_count+=line.count("Text\n")
	
	word_count+=len(line.split(" "))
	for letter in line:
		if(letter in vowels):
			v_count+=1
print(" Vowel: ",v_count,"\n","Number of Words: ",word_count)
print(" A count: ",a_count,"\n","Text: ",text_count)
print(" Space: ",space_count)
