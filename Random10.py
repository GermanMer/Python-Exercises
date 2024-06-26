#Exercise 10: Generate a random date between given start and end dates

import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", getRandomDate("5/1/1982", "11/01/2024"))
