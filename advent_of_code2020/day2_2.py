# Part 2
count = 0
def isValid(lst):
	minAndMax = lst[0].split("-")
	character = lst[1].replace(":","")
	password = lst[2]
	
	if(password[(int(minAndMax[0])-1)] == character or password[(int(minAndMax[1])-1)] == character):
		if(password[int(minAndMax[0])-1] != password[int(minAndMax[1])-1]):
			return(True)


with open("passwords.txt", "r") as file:
	for line in file:
		lst = line.split()
		
		if(isValid(lst)):
			count = count + 1

print(count)