# This is meant to be used to have it so that every month, it creates a newfile (csv/other format) so that it easier to check, where it can also be made so that the info on wheter a week overlaps between two months, is pointed out & taken into account for the overlap.
import datetime
from os import fork
from re import split
import string
import csv

# this is for the first digit of the clockin & out; 1 in 1200
possibleFirstFDigit = [0, 1, 2]
possibleNextDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
possibleFMin = [0, 1, 2, 3, 4, 5, 6]


def newFileCreation():
    # Meant so that every month the file changes
    print("File Made: ")


def constantFile():
    constant_data = []
    with open("constants.csv", "r") as file:
        data = file.readlines()
    file.close
    # print("Data:", data)
    for item in data:
        item = item.split(",")
        constant_data.append(item)

    print(constant_data)
    for item in constant_data:
        while(item[1] == f"\n"):
            print(f"Please Input {item[0]}:")
            if 



def openingExsistingFile(fileName):
    try:
        with open(fileName, "r") as file:
            testData = file.readlines
            fileState = "File Opened"
            print(fileState)
        file.close
    except IOError:
        fileState = "File NOT exsist"
        print(fileState)

    filepath = fileName
    title = fileName[:-4]

    if fileState == "File NOT exsist":
        insertedPlaceholder = "This is a new file: " + title
        with open(filepath, mode="w", newline="") as file:
            file.writelines(insertedPlaceholder)
        print("New File as been created")

    else:
        with open(filepath, mode="r") as file:
            data = file.readlines()
            print(data)

    return fileState, title


# This will check whether a new file has to be made or not!
def inputClocker(InOut):
    while True:
        clocker = input("Clock " + InOut + "  Time (24-hr):")
        try:
            clocker = int(clocker)
        except ValueError:
            print("!ERROR! Only Integer value")

        # after this; clockin is an int
        clocker = str(clocker)
        if len(clocker) == 4:
            if (
                int(clocker[0]) in possibleFirstFDigit
                or int(clocker[1]) in possibleNextDigits
                or int(clocker[2]) in possibleFMin
                or int(clocker[3]) in possibleNextDigits
            ):
                break
            else:
                print("~Please Enter a Valid Time~")
        else:
            print("Please Enter a 4 digit No.")
    # print(clocker)

    return clocker


def converter(insertedTime):
    hour = insertedTime[0] + insertedTime[1]
    minute = insertedTime[2] + insertedTime[3]

    minuteFraction = int(minute) / 60

    fixedTime = int(hour) + minuteFraction
    return fixedTime


def Calculator(clockIn, clockOut):
    payPerHour = 11

    # this doesnt include break
    breakTime = 0
    if clockIn < 12:
        breakTime += 1
    if clockOut > 19.5:
        breakTime += 1
    totalHours = clockOut - clockIn - breakTime
    payForDay = payPerHour * totalHours

    return payForDay


def fileEditor(fileName, payForDay, currentDate, clockInFixed, clockOutFixed):
    print("File is going to be edited")
    currentDateFixed = f"{currentDate[-1]}-{currentDate[-2]}-{currentDate[-3]}"
    data = [currentDateFixed, clockInFixed, clockOutFixed, payForDay]
    data_to_be_added = ""
    for item in data:
        item = str(item)
        data_to_be_added += f",{item}"
    data_to_be_added = data_to_be_added[1:]
    print(data_to_be_added)  # data_to_be_added = str(data_to_be_added)
    with open(fileName, mode="a", newline="") as file:
        file.writelines(data_to_be_added)
        file.close


fileCurrent = constantFile()

# this variable is the current date; got it from CHATGPT
# Its time is a class apparently,, will get back to that when i figure out the difference :)
currentDate = datetime.date.today()
# this works, has been checked
currentDate = str(currentDate)
currentDate = currentDate.split("-")

print(currentDate)


# File is YYYY-MM
fileName = currentDate[1] + "-" + currentDate[0] + ".csv"
print(fileName)

fileState, title = openingExsistingFile(fileName)
clockIn = inputClocker("In")
clockOut = inputClocker("Out")

# print(fileState + "   " + title)

clockInFixed = converter(clockIn)
clockOutFixed = converter(clockOut)

payForDay = Calculator(clockInFixed, clockOutFixed)
print("$", payForDay)

edit_of_File = fileEditor(fileName, payForDay, currentDate, clockInFixed, clockOutFixed)
