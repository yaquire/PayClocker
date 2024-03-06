#This is meant to be used to have it so that every month, it creates a newfile (csv/other format) so that it easier to check, where it can also be made so that the info on wheter a week overlaps between two months, is pointed out & taken into account for the overlap.
import datetime


print('This is a test')

def newFileCreation():
    #Meant so that every month the file changes
    print('File Made: ')

def openingExsistingFile():
    with open() as fileExisting:
        curentData = fileExisting.readlines
    print('File Opened')


#This will check whether a new file has to be made or not!

#this variable is the current date; got it from CHATGPT 
#Its time is a class apparently,, will get back to that when i figure out the difference :)
currentDate = datetime.date.today()
#this works, has been checked

#print('Current Date: ',(currentDate))


