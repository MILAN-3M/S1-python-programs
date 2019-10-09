string=str(input("enter the string:"))
vowel=0
consonent=0
non=0
for i in string:
	int c;
	c=i;
	if c>=65 and c<=90 or c>=97 and c<=122:
			
		if i=="a" or i=="e" or i=="o" or i=="i" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
			vowel=vowel+1

		else:
			consonent=consonent+1
	else:
		non+=1
print("no of vowels=",vowel)
print("no of non vowels=",consonent)
print("No of non alphabets=",non)
	
