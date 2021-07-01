import matplotlib.pyplot as plt
import os

#initializers
headers = []
times = []


def getData():
    print("Welcome to the kart timing plotter \nTo use copy the file with times in the same directory as this file\nIt is important that the times do not have letters or symbols on the same line and that the timings are sperated by a header(e.g. session1)\nEmpty lines are allowed to be in the txt file")
    data = openFile()
    index = -1
    for line in data:
        line = line.strip()
        if line != "":
            if isHeader(line):
                headers.append(line)
                times.append([])
                index +=1
            else:
                times[index].append(float(line))
    return
def plotData(amountOfYTicks):
    for i in range(0,len(times)):
        laps = range(0,len(times[i]))
        plt.plot(laps,times[i], marker='o', label=headers[i])
        plt.legend()
        plt.xlabel("lap")
        plt.ylabel("lap time")
        plt.xticks(laps)
        plt.yticks(getYTicks(times[i],amountOfYTicks))
    plt.show()
    plt.close()

def openFile():
    print("Which file would you like to open? \n(include the extension and the file should be in the same directory as this .py file)")
    while True:
        try:
            scriptName = os.path.basename(__file__)
            localPath = __file__
            localPath2 = localPath[:len(localPath) - len(scriptName)]
            #print(localPath2)
            txtName = input()
            filePath = localPath2  + txtName
            print(filePath)
            file = open(filePath, 'r', encoding='utf-8-sig')
            return file
        except(Exception):
            print("File not found try again\n(include the extension and the file should be in the same directory as this .py file)")

def isHeader(strToCheck):
    for char in strToCheck:
        if str(char).isalpha():
            return True
    return False
def getYTicks(t :list,amountOfYTicks:int):
    amountOfYTicks -= 2
    inBetween = []
    maxT = max(t)
    minT = min(t)
    diff = maxT - minT
    diffOnScale = diff/amountOfYTicks
    for x in range(-1,amountOfYTicks+1):
        inBetween.append(minT + x*diffOnScale)
    return inBetween





###main
#modifyable variables
amountOfYTicks = 20
#############
getData()
plotData(amountOfYTicks)
print(headers)
print(times)