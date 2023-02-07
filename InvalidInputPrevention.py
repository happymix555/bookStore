from datetime import datetime

#   isFloatValue
def allowOnlyFloat( userInput ):
    ''' check weather or not user input a number.

        ARGS: user input
    '''
    return isinstance( userInput, float )

    try:
        float( userInput )
        return True
    except:
        return False

#   isPositiveFloatValue
def allowOnlyPositiveFloat( userInput ):
    ''' check if user input a positive number( float or int).

        ARGS: user input
    '''
    return isinstance( userInput, float ) and userInput >= 0

    try:
        if float( userInput ) >= 0:
            return True
        else:
            return False
    except:
        return False


def allowOnlyInt( userInput ):
    ''' check if user input a integer.

        ARGS: user input
    '''

    try:
        int( userInput )
        return True
    except:
        return False
    
def allowOnlyPositiveInt( userInput ):
    ''' check if user input a positive integer.

        ARGS: user input
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

        ARGS: user input, lower bound , upper bound
    '''
    return lowerBound <= int(userInput) <= upperBound
    #     return True
    # else:
    #     return False

def checkValidDateStrFormat( dateStr ):
    ''' check if user input date with correct format.
        format is YYYY-MM-DD

        ARGS: user input
    '''
    try:
        datetime.strptime( dateStr, '%Y-%m-%d' )
    except ValueError:
        return False
    return True

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

        ARGS: date that is intended to be in the future, reference date.
    '''
    #   TODO: use datetime lib to compute this

    # convert string to datetime datatype.
    toBeLaterDate = datetime.strptime(toBeLaterDate, '%Y-%m-%d')
    currentDate = datetime.strptime(currentDate, '%Y-%m-%d')

    if toBeLaterDate.day - currentDate.day >= 1:
        return True
    else:
        return False

def findRecordObjectById( bookStoreObject, rentRecordIdInt ):
    ''' find rent record object by its id.

        ARGS: BookStore object, rent record id

        RETURN: RentRecord object
    '''

    for rentRecord in bookStoreObject.rentRecordStorage.rentRecordList:
        if rentRecord.rentRecordIdInt == rentRecordIdInt:
            return rentRecord

def fineBookObjectById( bookStoreObject, bookIdInt ):
    ''' find Book object by is id.

        ARGS: BookStore object, book id in int

        RETURN: Book object
    '''

    for book in bookStoreObject.bookStorage.bookList:
        if book.bookIdInt == bookIdInt:
            return book

def checkStringNotEmpty( inputStr ):
    ''' check if given string is empty or  not.

        ARGS: input string.

        RETURN: boolean
    '''

    # if string is empty return False.
    if inputStr.strip() == '':
        return False
    
    # if string is not empty return True.
    return True

