import re
import time

# HOLY SPAGHETIIIIIIIIIIIIIIIIIIIIIIII

validCount = 0
reqFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def hasAllFields(fields):
	for field in reqFields:
		if(field not in fields):
			return False


	return True;


def isValid(fields):
	passport = fields.replace("\n"," ")
	for field in passport.split(" "):
		keys = field.split(":")
		
		if(keys[0] == "byr"):
			if(len(keys[1]) != 4 or int(keys[1]) > 2002 or int(keys[1]) < 1920):
				return False
		if(keys[0] == "iyr"):
			if(len(keys[1]) != 4 or int(keys[1]) > 2020 or int(keys[1]) < 2010):
				return False
		
		if(keys[0] == "eyr"):
			if(len(keys[1]) != 4 or int(keys[1]) > 2030 or int(keys[1]) < 2020):
				return False
		
		if(keys[0] == "hgt"):
			if(keys[1][-2:] != "cm" and keys[1][-2:] != "in"):
				return False
		
		
			if(keys[1][-2:] == "cm"):
				if(int(keys[1][:-2]) < 150 or int(keys[1][:-2]) > 193):
					return False
			
			if(keys[1][-2:] == "in"):
				if(int(keys[1][:-2]) < 59 or int(keys[1][:-2]) > 76):
					return False
		
		if(keys[0] == "hcl"):
			if(not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', keys[1])):
				return False
		if(keys[0] == "ecl"):
			if(keys[1] != "amb" and keys[1] != "blu" and keys[1] != "brn" and keys[1] != "gry" and keys[1] != "grn" and keys[1] != "hzl" and keys[1] != "oth"):
				return False
				
		if(keys[0] == "pid"):
			if(not keys[1].isnumeric() or len(keys[1]) != 9):
				return False
	return True
with open("passports.txt", "r") as file:
	tmp = file.read()

passportList = tmp.split("\n\n")

for entry in passportList:
	if(hasAllFields(entry)):
		if(isValid(entry)):
			validCount = validCount + 1

print(validCount)