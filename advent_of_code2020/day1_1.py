lst = []

with open("input.txt", "r") as file:
	for num in file:
		stripped_line = num.strip()
		lst.append(int(stripped_line))


for entry in lst:
	target = 2020 - entry
	if(target in lst):
		print(target*entry)