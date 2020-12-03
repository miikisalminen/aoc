lst = []
posX = 0
treeCount = 0

# --- DAY 3 PART 1 ---

with open("map.txt", "r") as file:
	for line in file:
		line = line.strip()
		lst.append(line*40)

		
for line in lst:
	if(line[posX] == "#"):
		treeCount = treeCount + 1
	
	posX = posX + 3
	
	
print("I hit {0} trees. Ouch!".format(treeCount))