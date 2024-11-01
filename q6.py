def get_input():
	file = open("q6data.txt")
	data = file.read().split("\n")[0]
	
	return data


def isunique(string):
	

	setstring = set(string)
	if len(setstring) == len(string):
		return True
	return False


def find_marker(data,length):
	start = 0
	

	for i in range(len(data) - length):
		end = start + length

		if isunique(data[start:end]):
			
			break

		start += 1

	return end 


data = get_input()


print(" unique marker start from ",find_marker(data,4))
print(" unique marker 14 start from ",find_marker(data,14))



