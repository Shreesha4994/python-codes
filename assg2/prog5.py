#read last N lines from file
n = int(input("Enter N: "))
f = open("sample.txt","r")
lines = f.readlines()
last_lines = lines[-n:]
for line in last_lines:
	print(line,end="2")
