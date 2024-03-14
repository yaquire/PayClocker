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


def inputClock():
    while True:
        clockIn = input("Clock In Time (24-hr):")
        try:
            clockIn = int(clockIn)
        except ValueError:
            print("!ERROR! Only Integer value")

        # after this; clockin is an int
        clockIn = str(clockIn)
        if len(clockIn) == 4:
            if (
                int(clockIn[0]) in possibleFirstFDigit
                or int(clockIn[1]) in possibleNextDigits
                or int(clockIn[2]) in possibleFMin
                or int(clockIn[3]) in possibleNextDigits
            ):
                break
            else:
                print("~Please Enter a Valid Time~")
        else:
            print("Please Enter a 4 digit No.")
    print(clockIn)

    return clockIn


def inputClockOut():
    while True:
        clockOut = input("Clock Out Time (24-hr):")
        try:
            clockOut = int(clockOut)
        except ValueError:
            print("!ERROR! Only Integer value")

        # after this; clockin is an int
        clockOut = str(clockOut)
        if len(clockIn) == 4:
            if (
                int(clockOut[0]) in possibleFirstFDigit
                or int(clockOut[1]) in possibleNextDigits
                or int(clockOut[2]) in possibleFMin
                or int(clockOut[3]) in possibleNextDigits
            ):
                break
            else:
                print("~Please Enter a Valid Time~")
        else:
            print("Please Enter a 4 digit No.")
    print(clockOut)

    return clockOut


def converter(insertedTime):
    hour = insertedTime[0] + insertedTime[1]
    minute = insertedTime[2] + insertedTime[3]

    minuteFraction = int(minute) / 60
    

    fixedTime = int(hour) + minuteFraction
    return fixedTime


def Calculator(clockIn, clockOut):
    payPerHour = 11
    
    
    #this doesnt include break
    breakTime=0
    if clockIn<12:
        breakTime +=1
    if clockOut>19.5:
        breakTime+=1
    totalHours = clockOut-clockIn-breakTime
    payForDay=payPerHour*totalHours
    

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
clockIn = inputClock()
clockOut = inputClockOut()

clockInFixed = converter(clockIn)
clockOutFixed = converter(clockOut)

payForDay = Calculator(clockInFixed,clockOutFixed)
print('$', payForDay)
