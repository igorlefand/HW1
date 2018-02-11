list = [4,2,7,8,9,10,2,8,6]

def listSum_func(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


def listAvg_func(list):
    avg = 0
    sum = 0
    count = 0
    for i in list:
        sum = sum + i
        count += 1
    avg = sum/count
    return avg

print ("Summary of the list is " + str(listSum_func(list)))
print ("Average of the list is " + str(listAvg_func(list)))