#Used pprint for debugging
from pprint import pprint

def readFile():
    #This function returns the file as a list where every line is an element
    try:
        myFile = open("cars.dat.txt","r")
        #myFile = open(input("Please write the name of the file including extension: "),"r")
    except:
        print ("There is no such file")
        readFile()
    fileList = []
    for line in myFile:
        fileList.append(line)
    return fileList

def dataExtractor(list_,start,end):
    #This function uses substrings to create a list with only the data needed
    dataList = []
    for index in range(0,len(list_)):
        if index % 2 == 0:
            evenLine = list_[index]
            dataList.append(evenLine[start:end])
    return dataList

def avgInList(list_):
    #This function takes a list and returns the average of its elements
    avgSum = 0
    for element in list_:
        element = float(element)
        avgSum += element
    average = avgSum/len(list_)
    return average
#We create the list
csvFile = readFile()
'''
    Here we create the 3 lists that containg the data for
    Miles per Gallon in City and Highway and the average midrange
    Price of the vehicles
'''
cityMPG = dataExtractor(csvFile,52,54)

highwayMPG = dataExtractor(csvFile,55,57)

avgPrice = dataExtractor(csvFile,42,46)

#We take the values, get the average, then convert them to float

avgCityMPG = float("%.2f" % avgInList(cityMPG))

avgHighwayMPG = float("%.2f" % avgInList(highwayMPG))

avgPrice = float("%.2f" % avgInList(avgPrice))

#Simply print the results
print ("The average MPG in the city is: {}\n \
The average MPG in the Highway is: {}\n \
The average price of these cars is: {}".format(avgCityMPG,avgHighwayMPG,avgPrice))
