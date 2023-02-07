from datetime import datetime


def allowOnlyFloat( userInput ):
    ''' check weather or not user input a number.
    '''

    try:
        float( userInput )
        return True
    except:
        return False
    
def allowOnlyPositiveFloat( userInput ):
    ''' check if user input a positive number( float or int).
    '''

    try:
        if float( userInput ) >= 0:
            return True
        else:
            return False
    except:
        return False


def allowOnlyInt( userInput ):
    ''' check if user input a integer.
    '''

    try:
        int( userInput )
        return True
    except:
        return False
    
def allowOnlyPositiveInt( userInput ):
    ''' check if user input a positive integer.
    '''
    try:
        if int( userInput ) >= 0:
            return True
        else:
            return False
        
    except:
        return False
        
def checkIntInRange( userInput, lowerBound, upperBound ):
    ''' check if user input is in this range
    '''

    if lowerBound <= int(userInput) <= upperBound:
        return True
    else:
        return False

def checkValidDateFormat( userInputStr ):
    ''' check if user input date with correct format.
    '''

    userInputList = userInputStr.split( '-' )
    if len(userInputList) != 3:
        return False
    if allowOnlyPositiveInt( userInputList[ 0 ] ) and allowOnlyPositiveInt( userInputList[ 1 ] ) and allowOnlyPositiveInt( userInputList[ 2 ] ):
        if 1 <= int( userInputList[ 1 ] ) <= 12:
            if 1 <= int( userInputList[ 2 ] ) <= 31:
                return True
            else:
                return False
        else:
            return False

def checkLaterDate( toBeLaterDate, currentDate ):
    ''' check if toBeLaterDate is in the future compared to currentDate.
    '''

    # convert string to datetime datatype.
    toBeLaterDate = datetime.strptime(toBeLaterDate, '%Y-%m-%d')
    currentDate = datetime.strptime(currentDate, '%Y-%m-%d')

    if toBeLaterDate.day - currentDate.day >= 1:
        return True
    else:
        return False

def findRecordObjectById( bookStoreObject, rentRecordIdInt ):
    for rentRecord in bookStoreObject.rentRecordStorage.rentRecordList:
        if rentRecord.rentRecordIdInt == rentRecordIdInt:
            return rentRecord

def fineBookObjectById( bookStoreObject, bookIdInt ):
    for book in bookStoreObject.bookStorage.bookList:
        if book.bookIdInt == bookIdInt:
            return book

