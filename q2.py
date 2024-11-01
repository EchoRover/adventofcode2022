

code_to_real = {"A":"Rock","B":"Paper","C":"Scissor",
		"X":"Rock","Y":"Paper","Z":"Scissor"}

real_to_points = {"Rock":1,"Paper":2,"Scissor":3}



def whowinsAndPoints(a,b):
	if b == "Rock" and a == "Scissor":
		return 6
	if b == "Scissor" and  a == "Paper":
		return 6
	if b == "Paper" and a == "Rock":
		return 6

	return 0

def calculateScoreFromCode(a,b):
	real_oppent = code_to_real[a]
	real_you = code_to_real[b]

	# draw
	if real_oppent == real_you:
		score = real_to_points[real_you] + 3
		return score

	#else
	score = real_to_points[real_you] + whowinsAndPoints(real_oppent,real_you)

	return score




def getInput():

	file = open("q2data.txt")
	data = file.read().split("\n")

	return(data)


def get_total_score(data):
	tot_Score = 0

	for i in data:
		tot_Score += calculateScoreFromCode(i[0],i[-1])

	return tot_Score


dataIntput = getInput()

print("total score is ",get_total_score(dataIntput))


""" part 2 """

code_to_real = {"A":"Rock","B":"Paper","C":"Scissor",
		"X":0,"Y":3,"Z":6}

def what_To_put(oppent_play,need):
	if need == 3:
		return oppent_play

	if need == 6:
		match oppent_play:
			case "Rock":
				return "Paper"

			case "Paper":
				return "Scissor"

			case "Scissor":
				return "Rock"

	else:
		match oppent_play:
			case "Rock":
				return "Scissor"

			case "Paper":
				return "Rock"

			case "Scissor":
				return "Paper"
	
def getScore2(oppent_play,result):

	#adding result


	score = code_to_real[result]

	#coverting
	oppent_play = code_to_real[oppent_play]
	result = code_to_real[result]

	score += real_to_points[what_To_put(oppent_play,result)]

	return score


def get_total_score_round2(data):
	tot_Score = 0

	
	

	for i in data:
		
		#oppent_play = code_to_real[i[0]]
		#result_needed = code_to_real[i[-1]]

		tot_Score += getScore2(i[0],i[-1])

	return tot_Score





print("total score is round 2 ",get_total_score_round2(dataIntput))














