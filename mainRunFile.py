#This is meant to be used to have it so that every month, it creates a newfile (csv/other format) so that it easier to check, where it can also be made so that the info on wheter a week overlaps between two months, is pointed out & taken into account for the overlap.
import datetime
import string

print('This is a test')

def newFileCreation():
    #Meant so that every month the file changes
    print('File Made: ')

def openingExsistingFile(fileName):
    try:
        with open(fileName,'r') as fileExisting:
            curentData = fileExisting.readlines
            print('File Opened')
    except IOError:
        print('File NOT exsist!')

#This will check whether a new file has to be made or not!

def inputClock():
    while True:
        clockIn = input('Clock In Time (24-hr):')
        try:
            clockIn = int(clockIn)
            clockIn = str(clockIn)
            hours = clockIn[-1]+clockIn[1]
            hours = int(hours)
            minutes = clockIn[1]+clockIn[3]
            minutes = int(minutes)
            if hours<23 or minutes<60:
                break
            else:
                print('!ERROR!\nThe value is not a possible time\nTry Again')

        except ValueError:
            print('!ERROR! Only Integer value')

        
    print(clockIn)
        

#this variable is the current date; got it from CHATGPT 
#Its time is a class apparently,, will get back to that when i figure out the difference :)
currentDate = datetime.date.today()
#this works, has been checked
currentDate = str(currentDate)
currentDateList = currentDate.split('-')
print(currentDateList)
fileName = 'Month:'+currentDateList[-2]+' Year:'+currentDateList[0]+'.csv'

openingExsistingFile(fileName)
inputClock()
        
#print('Current Date: ',(currentDate))


