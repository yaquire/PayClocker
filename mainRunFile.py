# This is meant to be used to have it so that every month, it creates a newfile (csv/other format) so that it easier to check, where it can also be made so that the info on wheter a week overlaps between two months, is pointed out & taken into account for the overlap.
import datetime
import string

# this is for the first digit of the clockin & out; 1 in 1200
possibleFirstFDigit = [0, 1, 2]
possibleNextDigits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
possibleFMin = [0, 1, 2, 3, 4, 5, 6]


print("This is a test")


def newFileCreation():
    # Meant so that every month the file changes
    print("File Made: ")


def openingExsistingFile(fileName):
    try:
        with open(fileName, "r") as fileExisting:
            curentData = fileExisting.readlines
            print("File Opened")
    except IOError:
        print("File NOT exsist!")


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
    print(clocker)

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


# this variable is the current date; got it from CHATGPT
# Its time is a class apparently,, will get back to that when i figure out the difference :)
currentDate = datetime.date.today()
# this works, has been checked
currentDate = str(currentDate)
currentDateList = currentDate.split("-")
print(currentDateList)
fileName = "Month:" + currentDateList[-2] + " Year:" + currentDateList[0] + ".csv"

openingExsistingFile(fileName)
clockIn = inputClocker("In")
clockOut = inputClocker("Out")

clockInFixed = converter(clockIn)
clockOutFixed = converter(clockOut)

payForDay = Calculator(clockInFixed, clockOutFixed)
print("$", payForDay)
