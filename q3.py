
def getInput():

	file = open("q3data.txt")
	data = file.read().split("\n")	

	return(data)



def getpriority(item):
	key = "abcdefghijklmnopqrstuvwxyz"

	priority = key.index(item.lower()) + 1
	if item.islower():
		return priority

	return priority + 26




def findmissing(rucksack):
	part1 = rucksack[:len(rucksack)//2]
	part2 = rucksack[len(rucksack)//2:]


	for i in part1:
		if i in part2:
			return i



def gettotal(data):

	sum = 0

	for i in data:
		sum += getpriority(findmissing(i))

	return sum

def findcommoninthree(a,b,c):
	for i in a:
		if (i in b) and (i in c):
			return i


def gettotal_threesacks(data):

	total = 0
	for i in range(0,len(data),3):

		total += getpriority(findcommoninthree(data[i],data[i+1],data[i+2]))

	return total



data = getInput()


print("sum of priority is ",gettotal(data))
print("sum of when three sackspriority is ",gettotal_threesacks(data))













