validCount = 0
reqFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def isValid(fields):
	for field in reqFields:
		if(field not in fields):
			return False


	return True;
	
with open("passports.txt", "r") as file:
	tmp = file.read()

passportList = tmp.split("\n\n")

for entry in passportList:
	if(isValid(entry)):
		validCount = validCount + 1

print(validCount)