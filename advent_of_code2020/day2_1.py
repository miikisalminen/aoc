# Part 1
count = 0
def isValid(lst):
	minAndMax = lst[0].split("-")
	character = lst[1].replace(":","")
	password = lst[2]
	
	if(password.count(character) >= int(minAndMax[0]) and password.count(character) <= int(minAndMax[1])):
		return(True)


with open("passwords.txt", "r") as file:
	for line in file:
		lst = line.split()
		
		if(isValid(lst)):
			count = count + 1

print(count)