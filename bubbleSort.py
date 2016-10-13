from time import sleep
from random import randint
from pprint import pprint
def bubbleSort(userList):
    counter = 0
    print (userList)
    for times in range(len(userList)-1):
#        changed = False
        for i in range(0,len(userList)-1):
            if userList[i] > userList[i+1]:
                temp = userList[i]
                userList[i] = userList[i + 1]
                userList[i+1] = temp
                print(userList)
                counter += 1
#                changed = True
#            if not changed:
#                return userList
    print ("Done after {0} re sortings".format(counter + 1))
    return userList

def getNumbers():
    numbers = input("Give me some numbers, (Separate them by space): ")
    intList = []
    for i in numbers.split():
        try:
            int(i)
            intList.append(i)
        except:
            print("Only integers please")
            getNumbers()

    return intList

#bubbleSort(getNumbers())
randomList = []
for i in range(1000):
    randomList.append(randint(-999,999))
print (bubbleSort(randomList))
#new_list = list(i for i in range(0,100))
#print (bubbleSort(new_list[::-1]))
'''
    DONE
'''
