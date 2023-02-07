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
        bookCountInt += 1
    print( '\n' )

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
            bookCountInt += 1
    print( '\n' )

def printAllRentRecord():
    ''' Print all rent record in our store.
    '''

    global bookStore
    rentRecordCountInt = 1

    # loop to get all rent record in rent record storage.
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:

        # find book name with book id.
        for book in bookStore.bookStorage.bookList:
            if book.bookIdInt == rentRecord.rentedBookIdInt:
                bookNameStr = book.bookNameStr

        # print various information
        print( f'{ rentRecordCountInt }. Renter Name: { rentRecord.renterNameStr } Rent Date: { rentRecord.rentDate } Expected Return Date: {rentRecord.expectedReturnDate} Actual return date: {rentRecord.actualReturnDate} Total Revenue: {rentRecord.thisRentRevenueFloat}' )
        print( f'   Rent price: { rentRecord.totalRentPrice } Fine: { rentRecord.totalFine } Rent Id: { rentRecord.rentRecordIdInt }' )
        print( f'   Rented book: { bookNameStr }' )
        rentRecordCountInt += 1
    print( '\n' )

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
            rentRecordCountInt += 1
    print( '\n' )

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
    
    # print all book currently in out store.
    print( 'Now we have these books in our store: ' )
    for book in bookStore.bookStorage.bookList:
        print( book.bookNameStr )
    state = 'start'
    print( '\n' )

def removeBook():
    ''' Remove a book from our store.
    '''

    global bookStore, state
    
    # print all book in our store to user with index.
    bookCountInt = 0
    allBookIdList = []
    for book in bookStore.bookStorage.bookList:
        allBookIdList.append( book.bookIdInt )
        print( f'{ bookCountInt + 1 }. Book name: { book.bookNameStr } Book ID: { book.bookIdInt }.' )
        bookCountInt += 1

    # get input from user in form of index of which book to be removed.
    bookIdToBeRemovedTest = TestValidInput()
    bookIdToBeRemovedTest.addInputText( 'Book to be removed: ' )

    # check if input is a positive integer
    bookIdToBeRemovedTest.addValidationFunction( allowOnlyPositiveInt ) 
    bookIdToBeRemovedTest.addErrorMessage( 'Error: Input can only be a positive integer' )

    # check if input is in bookCountInt's range to ensure that user select only the book that
    # exist in our store.
    bookIdToBeRemovedTest.addValidationFunction( checkIntInRange, [1, bookCountInt] )
    bookIdToBeRemovedTest.addErrorMessage( 'This book dose not exist.' )
    bookIndexToBeRemovedInt = bookIdToBeRemovedTest.executeAllValidation()

    bookStore.bookStorage.removeBook( int( allBookIdList[ int( bookIndexToBeRemovedInt ) - 1 ] ) )
    print( 'Book was removed successfully.' )
    print( 'This is all book left in our store.' )
    printAllBookInStore()
    print( '\n' )
    state = 'start'
    

def rentBook():
    ''' rent a book in our book store
    '''
    global bookStore, state

    # print all available book for user to be choose and get all available book id.
    bookCountInt = 0
    allBookAvailableIdList = []
    for book in bookStore.bookStorage.bookList:
        if book.availableStatus == True:
            allBookAvailableIdList.append( book.bookIdInt )
            print( f'{ bookCountInt + 1 }. Book name: { book.bookNameStr } Book ID: { book.bookIdInt }.' )
            bookCountInt += 1

    # get check if user input a positive integer
    rentBookIndexTest = TestValidInput()
    rentBookIndexTest.addInputText( 'Book to be rent: ' )
    rentBookIndexTest.addValidationFunction( allowOnlyPositiveInt )
    rentBookIndexTest.addErrorMessage( 'Error: input must be only positive int' )

    # check if this book exist in out store
    rentBookIndexTest.addValidationFunction( checkIntInRange, [1, bookCountInt] )
    rentBookIndexTest.addErrorMessage( 'Error: this book does not exist.' )
    rentBookIndexInt = rentBookIndexTest.executeAllValidation()

    # get renter name
    renterName = input( 'Renter name: ' )

    # get and validate rent date
    rentDateTest = TestValidInput()
    rentDateTest.addInputText( '(YYYY-M-D)Rent Date:' )
    rentDateTest.addValidationFunction( checkValidDateFormat )
    rentDateTest.addErrorMessage( 'Error: incorrect date.' )
    rentDate = rentDateTest.executeAllValidation()

    # get and validate expected return date
    expectedReturnDateTest = TestValidInput()

    # check expected date format
    expectedReturnDateTest.addInputText( '(YYYY-M-D)Expected return Date:' )
    expectedReturnDateTest.addValidationFunction( checkValidDateFormat )
    expectedReturnDateTest.addErrorMessage( 'Error: incorrect date.' )

    # check if expected return date is in the future compared to rent date.
    expectedReturnDateTest.addValidationFunction( checkLaterDate, [ rentDate ] )
    expectedReturnDateTest.addErrorMessage( 'Error: expected return date must be in the future.' )
    expectedReturnDate = expectedReturnDateTest.executeAllValidation()

    bookStore.rentRecordStorage.rentBook( renterName, datetime.strptime(rentDate, '%Y-%m-%d'), 
    datetime.strptime(expectedReturnDate, '%Y-%m-%d'), int( allBookAvailableIdList[ int( rentBookIndexInt ) - 1 ] ), bookStore.bookStorage, bookStore.rentRecordStorage )
    print( 'Rent successfully.' )
    printAllRentRecord()
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