import FileInterface as fi
import DatabaseInterface as di
import random

numberArray = []
curNum = 0
maxRow = 0

def generateNewRandomNumbers(rowCount):
    global numberArray
    curNum = 0
    maxRow = rowCount
    numberArray = random.sample(xrange(1,maxRow), maxRow-1)


def nextRandomNumber():
    global curNum
    try:
        value = numberArray[curNum]
    except IndexError:
        generateNewRandomNumbers(maxRow)
        value = numberArray[curNum]
    curNum=curNum+1
    return value

#OUTPUT: string to be sent off
#FUNCTION: to send a pashto word and it's paired enligh meaning
def ex():
    global maxRow
    database = di.getDatabase("pashto.db")
    if maxRow == 0:
        maxRow = di.getMaxIndex(database)
    randRow = nextRandomNumber()
    wordPair = di.getWordPair(database, randRow)
    englishValue = wordPair[0]
    pashtoValue = wordPair[1]
    outputString = "Pashto: " + pashtoValue + "\nEnglish: " + englishValue
    return outputString
