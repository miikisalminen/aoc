lst = []

with open("input.txt", "r") as file:
	for num in file:
		stripped_line = num.strip()
		lst.append(int(stripped_line))

		
def searchForSumOfThree () :
	for entry in lst:
		for i in range(1,len(lst)):
			for j in range(2,len(lst)):
				if(2020 - entry - lst[i] - lst[j] == 0):
					return(entry*lst[i]*lst[j])

print(searchForSumOfThree())






