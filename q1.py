

def get_data():
    file = open("q1data.txt")
    data = file.read().split("\n")

    #print(data)
    return data



def condense(data):
    new_data = [0]

    for i in data:
        #print(new_data)
        if i.isdigit():
            #print(i)
            new_data[-1] += int(i)

        else:
            new_data.append(0)

    return new_data


def getmaxthree(list):
    list.sort(reverse = True)
    return sum(list[:3])


text_data = get_data()

final_data = condense(text_data)

print(f"max calorie carried  = {max(final_data)}")


print(f"max calorie carried by top 3 total is = {getmaxthree(final_data)}")