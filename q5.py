def get_input():
	file = open("q5data.txt")
	data = file.read().split("\n")


	#separate the parts

	stack_part = data[:data.index("")]
	moves = data[data.index("")+1:]

	#stacks creation
	stack_part.reverse()
	stacksno = len(stack_part[0].split())
	stack_part.pop(0)


	for i in range(stacksno):
		
		stacks[i + 1] = []

	for layer in stack_part:
		index = 1
		for i in range(1,len(layer),4):
			
			if not layer[i] == " ":
				stacks[index].append(layer[i])
			index += 1

	#giveing moves
	return moves

def do_a_move(move):
	move = move.split()

	times = int(move[1])
	startpoint = int(move[3])
	endpoint = int(move[5])

	for i in range(times):
		item = stacks[startpoint].pop()
		stacks[endpoint].append(item)




	#print(times,startpoint,endpoint)

def do_all_moves_and_get_tops(moves):
	for move in moves:
		do_a_move(move)

	code = ""

	for i in stacks.values():
		code += i[-1]

	return code



stacks = dict()

moves = get_input()


code = do_all_moves_and_get_tops(moves)

print("the code is cratemover 9000 ",code)

##################################

def do_a_move_9001(move):
	move = move.split()

	times = int(move[1])
	startpoint = int(move[3])
	endpoint = int(move[5])

	items = stacks[startpoint][-times:]
	stacks[startpoint] = stacks[startpoint][:-times]
	stacks[endpoint].extend(items)


def do_all_moves_and_get_tops_9001(moves):
	for move in moves:
		do_a_move_9001(move)

	code = ""

	for i in stacks.values():
		code += i[-1]

	return code


stacks = dict()

moves = get_input()


code = do_all_moves_and_get_tops_9001(moves)

print("the code is cratemover 9001 ",code)







