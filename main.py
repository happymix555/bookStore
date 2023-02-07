from BookStore import BookStore

from datetime import datetime
from datetime import date
from InvalidInputPrevention import *
from TestValidInput import *


def printAllBookInStore():
    ''' Print all book in our store.
    '''

    global bookStore
    bookCountInt = 1

    # loop to get each book object.
    for book in bookStore.bookStorage.bookList:
        
        # print various information about this book.
        print( f'{bookCountInt}. Book name: {book.bookNameStr} Book ID: {book.bookIdInt}.' )
        print( '\n' )
        bookCountInt += 1

def printAllAvailableBook():
    ''' Print all book in our store that is currently available for rent.
    '''

    global bookStore
    bookCountInt = 1

    # loop to get each book object.
    for book in bookStore.bookStorage.bookList:

        # if this book is available then print it.
        if book.availableStatus == True:
            print( f'{bookCountInt}. Book name: {book.bookNameStr} Book ID: {book.bookIdInt}.' )
            print( '\n' )
            bookCountInt += 1

def printAllRentRecord():
    ''' Print all rent record in our store.
    '''

    global bookStore
    rentRecordCountInt = 1

    # loop to get all rent record in rent record storage.
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:

        # print various information
        print( f'{ rentRecordCountInt }. Renter Name: { rentRecord.renterNameStr } Rent Date: { rentRecord.rentDate } Expected Return Date: {rentRecord.expectedReturnDate} Actual return date: {rentRecord.actualReturnDate} Total Revenue: {rentRecord.thisRentRevenueFloat}' )
        print( f'Rent price: { rentRecord.totalRentPrice } Fine: { rentRecord.totalFine } Rent Id: { rentRecord.rentRecordIdInt }' )
        print( '\n' )
        rentRecordCountInt += 1

def printUnreturnedRentRecord():
    ''' Print all rent record that has not been returned yet.
    '''

    global bookStore4
    rentRecordCountInt = 1

    # loop to get each rent record object.
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:

        #if this rent record has not been returned then print it
        if rentRecord.actualReturnDate == None:
            thisBookObject = fineBookObjectById( bookStore, rentRecord.rentedBookIdInt )
            print( f'{rentRecordCountInt}. Renter Name: {rentRecord.renterNameStr} Book Name: { thisBookObject.bookNameStr } Rent Date: {rentRecord.rentDate} Expected Return Date: {rentRecord.expectedReturnDate} Actual return date: {rentRecord.actualReturnDate} Total Revenue: {rentRecord.thisRentRevenueFloat} Rent Id: {rentRecord.rentRecordIdInt}' )
            print( '\n' )
            rentRecordCountInt += 1

def addBook():
    ''' Add new book to our store.
    '''

    global bookStore, state

    # get book name from user.
    thisBookNameStr = input( 'Book name: ' )

    # get rent price per day of this book through TestValidInput class.
    testBookPricePerDayFloat = TestValidInput()
    testBookPricePerDayFloat.addInputText( 'Book rent price per Day: ' )
    
    # check if book rent price is only a positive float.
    testBookPricePerDayFloat.addValidationFunction( allowOnlyPositiveFloat )
    testBookPricePerDayFloat.addErrorMessage( 'Error: input can only be a positive number.' )
    thisBookPricePerDayFloat = testBookPricePerDayFloat.executeAllValidation()
    
    # get fine rate of this book through TestValidInput class.
    testBookFineRateFloat = TestValidInput()
    testBookFineRateFloat.addInputText( 'Book fine rate: ' )
    
    # check if fine rate is only a positive float.
    testBookFineRateFloat.addValidationFunction( allowOnlyPositiveFloat )
    testBookFineRateFloat.addErrorMessage( 'Error: input can only be a positive number.' )
    thisBookFineRateFloat = testBookFineRateFloat.executeAllValidation()

    # create Book object and add it to a BookStorage in BookStore.
    bookStore.bookStorage.addBook( thisBookNameStr, float( thisBookPricePerDayFloat ), float( thisBookFineRateFloat ),
                                    bookStore.bookStorage)
    print( 'Now we have these books in our store: ' )
    for book in bookStore.bookStorage.bookList:
        print( book.bookNameStr )
    state = 'start'
    print( '\n' )

def removeBook():
    global bookStore, state
    bookCountInt = 1
    allBookIdList = []
    for book in bookStore.bookStorage.bookList:
        allBookIdList.append( book.bookIdInt )
        print( f'{bookCountInt}. Book name: {book.bookNameStr} Book ID: {book.bookIdInt}.' )
        bookCountInt += 1
    bookIdToBeRemovedInt = input( 'Book ID to be removed: ' )
    if allowOnlyPositiveInt( bookIdToBeRemovedInt ):
        if int( bookIdToBeRemovedInt ) not in allBookIdList:
            print( 'This book was not found in our store.' )
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
    printAllAvailableBook()
    allBookAvailableIdList = []
    for book in bookStore.bookStorage.bookList:
        if book.availableStatus == True:
            allBookAvailableIdList.append( book.bookIdInt )
    rentBookIdInt = input( 'Book ID to rent: ' )
    if allowOnlyPositiveInt( rentBookIdInt ):
        if int( rentBookIdInt ) not in allBookAvailableIdList:
            print( 'This book dose not exist.' )
        else:
            renterName = input( 'Renter name: ' )
            rentDate = input( '(YYYY-M-D)Rent Date:' )
            if checkValidDateFormat( rentDate ):
                expectedReturnDate = input( '(YYYY-M-D)Expected Return Date:' )
                if checkValidDateFormat( expectedReturnDate ):
                    if checkLaterDate( datetime.strptime(rentDate, '%Y-%m-%d'), datetime.strptime(expectedReturnDate, '%Y-%m-%d') ):
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
    printUnreturnedRentRecord()
    allUncloseRentRecordList = []
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:
        if rentRecord.actualReturnDate == None:
            allUncloseRentRecordList.append( rentRecord.rentRecordIdInt )
    if allUncloseRentRecordList != []:
        rentIdToBeReturn = input( 'Rent ID to return: ' )
        if allowOnlyPositiveInt( rentIdToBeReturn ):
            if int( rentIdToBeReturn ) not in allUncloseRentRecordList:
                print( 'This rent record was not found in our store.' )
            else:
                rentRecordObject = findRecordObjectById( bookStore, int( rentIdToBeReturn ) )
                rentDate = rentRecordObject.rentDate
                actualReturnDate = input( '(YYYY-M-D)Return date: ' )
                if checkValidDateFormat( actualReturnDate ):
                    if checkLaterDate( rentDate, datetime.strptime(actualReturnDate, '%Y-%m-%d') ):
                        bookStore.rentRecordStorage.returnBook( datetime.strptime(actualReturnDate, '%Y-%m-%d'), int(rentIdToBeReturn), bookStore.bookStorage )
                        print( 'Return successfully.' )
                        printAllRentRecord()
                        state = 'start'
    else:
        print( 'There is no rent record at this time.' )
        state = 'start'

    # if rentIdToBeReturn == 'x':
    #     state = 'start'

def viewTotalRevenueInDateRange():
    global bookStore, state
    startDate = input( '(YYYY-M-D)Start date: ' )
    if checkValidDateFormat( startDate ):
        endDate = input( '(YYYY-M-D)End date: ' )
        if checkValidDateFormat( endDate ):
            if checkLaterDate( datetime.strptime(startDate, '%Y-%m-%d'), datetime.strptime(endDate, '%Y-%m-%d') ):
                revenueInThisDateRange = bookStore.calculateTotalRevenueInDateRange( datetime.strptime(startDate, '%Y-%m-%d'), datetime.strptime(endDate, '%Y-%m-%d') )
                print( f'Total Revenue in this date range is: {revenueInThisDateRange}' )
                state = 'start'

def viewTheMostPopularBook():
    global bookStore, state
    bookNameList, bookNumberOfRentList = bookStore.viewTheMostPopularBook()
    popularityNumberInt = 1
    for bookIndex in range( len( bookNameList ) ):
        print( f'{ popularityNumberInt }. Book name: { bookNameList[ bookIndex ] }, Number of rent times: { bookNumberOfRentList[ bookIndex ] }' )
        popularityNumberInt += 1
    # print( bookNameList )
    # print( bookNumberOfRentList )
    state = 'start'


#main loop

bookStore = BookStore()


#adding book to store
bookStore.bookStorage.addBook( 'book1', float( 10 ), float( 1.5 ),
    bookStore.bookStorage )
bookStore.bookStorage.addBook( 'book2', float( 15 ), float( 1.5 ),
    bookStore.bookStorage )
bookStore.bookStorage.addBook( 'book3', float( 20 ), float( 1.5 ),
    bookStore.bookStorage )

# #renting book
# bookStore.rentRecordStorage.rentBook( 'happymix', date(2023-2-3), 
#     date(2023-2-4), 0, bookStore.bookStorage, bookStore.rentRecordStorage )



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

    elif state == '5':
        viewTotalRevenueInDateRange()

    elif state == '6':
        viewTheMostPopularBook()