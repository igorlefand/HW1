list = [4,2,7,8,9,10,2,8,6]

def listSum_func(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


    
print ("Summary of the list is " + str(listSum_func(list)))