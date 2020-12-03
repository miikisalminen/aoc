lst = []
positions = [0,0,0,0,0]
treeCounts = [0,0,0,0,0]
everyOther = True

# --- DAY 3 PART 2 ---

with open("map.txt", "r") as file:
	for line in file:
		line = line.strip()
		lst.append(line*100)

		
for line in lst:

	# Checking first slope 1:1
	if(line[positions[0]] == "#"):
		treeCounts[0] = treeCounts[0] + 1
	# Checking second slope 3:1
	if(line[positions[1]] == "#"):
		treeCounts[1] = treeCounts[1] + 1
	# Checking third slope 5:1
	if(line[positions[2]] == "#"):
		treeCounts[2] = treeCounts[2] + 1
	# Checking fourth slope 7:1
	if(line[positions[3]] == "#"):
		treeCounts[3] = treeCounts[3] + 1
	# Checking fifth slope 1:2
	if(line[positions[4]] == "#" and everyOther):
		treeCounts[4] = treeCounts[4] + 1
	
	# Updating positions
	positions[0] = positions[0] + 1
	positions[1] = positions[1] + 3
	positions[2] = positions[2] + 5
	positions[3] = positions[3] + 7
	everyOther = not everyOther
	if(everyOther):
		positions[4] = positions[4] + 1

print(treeCounts[0]*treeCounts[1]*treeCounts[2]*treeCounts[3]*treeCounts[4])