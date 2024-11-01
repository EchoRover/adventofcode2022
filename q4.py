
def get_input():

	file = open("q4data.txt")
	data = file.read().split("\n")
	data = [tuple(i.split(",")) for i in data]
	return(data)


def genrange(code,a = 0 ):
	begin = int(code[:code.index("-")])
	end = int(code[code.index("-") + 1:])

	if a:
		return begin,end

	#print(begin,end)

	
	trange = [i for i in range(begin,end + 1)]
	return(trange)

"""
def is_one_inside_other(pair):

	part1 = "".join(map(str,genrange(pair[0])))
	part2 = "".join(map(str,genrange(pair[1])))

	#print(part1,part2,part2 in part1,part1 in part2)
	print(part1)
	print(part2)

	if (part1 in part2) or (part2 in part1):
		print(part1,part2)
		return 1
	return 0




def temp(pair):


	if pair[0] == pair[1]:
		return 1
	p1begin,p1end = genrange(pair[0],1)
	p2begin,p2end = genrange(pair[1],1)

	if p1begin < p2begin:
		bigger = p1end
		smaller = p2end
	else:
		bigger = p2end
		smaller = p1end

	if bigger >= smaller:
		return 1

	print(pair)
	return 0






def get_total_repeats(data):
	total = 0

	for i in data:
		total += temp(i)
		is_one_inside_other(i)

	return total


"""
data = get_input()


def temp3(pair):
	part1 = genrange(pair[0])
	part2 = genrange(pair[1])

	#print(part1,part2)

	# i in 2

	for i in part1:
		if i not in part2:
			break
	else:
		return 1

	## 2 in 1

	for i in part2:
		if i not in part1:
			break
	else:
		return 1

	return 0


def temp4(pair):
	part1 = genrange(pair[0])
	part2 = genrange(pair[1])

	#print(part1,part2)

	# i in 2

	for i in part1:
		if i in part2:
			return 1
	return 0




def get_total_repeats(data):
	total = 0

	for i in data:
		total += temp3(i)

	return total



def get_total_repeats_no_overlap(data):
	total = 0

	for i in data:
		total += temp4(i)

	return total	

print("the no of full overlap is ", get_total_repeats(data))
print("the no of any overlap ", get_total_repeats_no_overlap(data))




