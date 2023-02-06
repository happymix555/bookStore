from BookStore import BookStore

from datetime import datetime
from datetime import date



def printAllBookInStore():
    global bookStore
    bookCountInt = 1
    for book in bookStore.bookStorage.bookList:
        print( f'{bookCountInt}. Book name: {book.bookNameStr} Book ID: {book.bookIdInt}.' )
        bookCountInt += 1

def stringToRentDateFormat( userInputString ):
    # userInPutString will be in format YYYY-M-D
    stringToList = userInputString.split('-')
    year = stringToList[0]
    month = stringToList[1]
    day = stringToList[2]
    return year, month, day

def printAllRentRecord():
    global bookStore
    rentRecordCountInt = 1
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:
        print( f'{rentRecordCountInt}. Renter Name: {rentRecord.renterNameStr} Rent Date: {rentRecord.rentDate} Expected Return Date: {rentRecord.expectedReturnDate} Actual return date: {rentRecord.actualReturnDate} Total Revenue: {rentRecord.thisRentRevenueFloat} Rent Id: {rentRecord.rentRecordIdInt}' )
        rentRecordCountInt += 1

def addBook():
    global bookStore, state
    thisBookNameStr = input( 'Book name: ' )
    thisBookPricePerDayFloat = input( 'Book rent price per Day: ' )
    thisBookFineRateFloat = input( 'Book fine rate: ' )
    bookStore.bookStorage.addBook( thisBookNameStr, float( thisBookPricePerDayFloat ), float( thisBookFineRateFloat ),
    bookStore.bookStorage )
    for book in bookStore.bookStorage.bookList:
        print( book.bookNameStr )
        print( book.bookIdInt )
        print( '\n' )
    state = 'start'

    if thisBookNameStr == 'x':
        state = 'start'

def removeBook():
    global bookStore, state
    bookCountInt = 1
    allBookIdList = []
    for book in bookStore.bookStorage.bookList:
        allBookIdList.append( book.bookIdInt )
        print( f'{bookCountInt}. Book name: {book.bookNameStr} Book ID: {book.bookIdInt}.' )
        bookCountInt += 1
    bookIdToBeRemovedInt = input( 'Book ID to be removed: ' )
    if int(bookIdToBeRemovedInt) not in allBookIdList:
        print( 'This book was not found in our store.' )
        state = 'start'
    else:
        bookStore.bookStorage.removeBook( int(bookIdToBeRemovedInt) )
        print( 'Book was removed successfully.' )
        print( 'This is all book left in our store.' )
        printAllBookInStore()
        state = 'start'

    if bookIdToBeRemovedInt == 'x':
        state = 'start'

def rentBook():
    global bookStore, state
    printAllBookInStore()
    rentBookIdInt = input( 'Book ID to rent: ' )
    renterName = input( 'Renter name: ' )
    rentDate = input( '(YYYY-M-D)Rent Date:' )
    expectedReturnDate = input( '(YYYY-M-D)Expected Return Date:' )
    rentDateObject = datetime.strptime(rentDate, '%Y-%m-%d')
    bookStore.rentRecordStorage.rentBook( renterName, rentDateObject, 
    datetime.strptime(expectedReturnDate, '%Y-%m-%d'), int(rentBookIdInt), bookStore.bookStorage, bookStore.rentRecordStorage )
    print( 'Rent successfully.' )
    printAllRentRecord()
    state = 'start'

    if rentBookIdInt == 'x':
        state = 'start'

def returnBook():
    global bookStore, state
    printAllRentRecord()
    rentIdToBeReturn = input( 'Rent ID to return: ' )
    actualReturnDate = input( '(YYYY-M-D)Return date: ' )
    bookStore.rentRecordStorage.returnBook( datetime.strptime(actualReturnDate, '%Y-%m-%d'), int(rentIdToBeReturn), bookStore.bookStorage )
    print( 'Return successfully.' )
    printAllRentRecord()
    state = 'start'

    if rentIdToBeReturn == 'x':
        state = 'start'




#main loop

bookStore = BookStore()

state = 'start'
while 1:
    if state == 'start':
        print( 'Welcome to Yannix book store.' )
        print( 'Please select the option that you want.' )
        print( '1. Add new book.' )
        print( '2. Remove a book.' )
        print( '3. Rent a book.' )
        print( '4. Return a book.' )
        print( '5. View total revenue in date range.' )
        print( '6. View the most popular books.' )
        state = 'waitStartInput'

    elif state == 'waitStartInput':
        state = input( 'Your command is: ' )
        if state not in [ '1', '2', '3', '4', '5', '6']:
            print( 'Incorrect Choice.' )
            state = 'waitStartInput'
    
    elif state == '1':
        addBook()
    
    elif state == '2':
        removeBook()

    elif state == '3':
        rentBook()

    elif state == '4':
        returnBook()