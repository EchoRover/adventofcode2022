
def getInput():

    file = open("q8data.txt")

    data = file.read().split("\n")

    return data 



def isvisble(plot,x,y,constraintx,constrainty):
    value = plot[y][x]

    pointerx,pointery = x,y 
    #right

    for i in range(constraintx - x):

        pointerx += 1

        #print("abc",plot[pointery][pointerx],value)
        if plot[pointery][pointerx] >= value:
            break
    else:
        return True

     

    # left
    pointerx = x
    for i in range(x - 0):
        pointerx -= 1
        if plot[pointery][pointerx] >= value:
            break
    else:
        return True


    #top

    pointerx,pointery = x,y
    for i in range(y - 0):
        pointery -= 1
        if plot[pointery][pointerx] >= value:
            break
    else:
        return True 

    #botton
    pointerx,pointery = x,y
    for i in range(constrainty - y):
        pointery += 1
        if plot[pointery][pointerx] >= value:
            break
    else:
        return True 

    return False

def scene_Score(plot,x,y,constraintx,constrainty):
    value = plot[y][x] 
    score = 1

    pointerx,pointery = x,y 
    #right
    part = 0

    for i in range(constraintx - x):

        pointerx += 1
        part += 1

        #print("abc",plot[pointery][pointerx],value)
        if plot[pointery][pointerx] >= value:
            break
    score *= part

     

    # left
    pointerx = x

    part = 0
    for i in range(x - 0):
        pointerx -= 1
        part += 1

        if plot[pointery][pointerx] >= value:
            break
    score *= part
    


    #top

    pointerx,pointery = x,y
    part = 0

    for i in range(y - 0):
        pointery -= 1
        part += 1
        if plot[pointery][pointerx] >= value:
            break
    score *= part
     

    #botton
    pointerx,pointery = x,y
    part = 0

    for i in range(constrainty - y):
        pointery += 1
        part += 1
        if plot[pointery][pointerx] >= value:
            break
    score *= part
    

    return score



def findvisible(trees):
    
    visible = 0
    length = len(trees[0]) 
    breadth = len(trees) 
    visible += length * 2
    visible += 2 * (breadth - 2)

    


    for row in range(breadth - 2):
        for column in range(length - 2):

            #print(trees[row + 1][column + 1],end = "")
            #print(isvisble(trees,column + 1,row + 1,length - 1,1))
            if isvisble(trees,column + 1,row + 1,length - 1,breadth - 1):
                visible += 1

        
            

    print("visible trees "+str(visible))

def FINDhighest(trees):
    
    score = 0
    length = len(trees[0]) 
    breadth = len(trees) 
    
    


    for row in range(breadth - 2):
        for column in range(length - 2):

            #print(trees[row + 1][column + 1],end = "")
            #print(isvisble(trees,column + 1,row + 1,length - 1,1))
            scene_score = scene_Score(trees,column + 1,row + 1,length - 1,breadth - 1)

            if scene_score > score:
                score  = scene_score

        
            

    print("FINDhighest scene_Score trees "+str(score))

data = getInput()
findvisible(data)
FINDhighest(data)




