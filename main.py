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

    # create book name test object
    bookNameStrTest = TestValidInput()
    bookNameStrTest.addInputText( 'Book name: ' )
    bookNameStrTest.addValidationFunction( checkStringNotEmpty )
    bookNameStrTest.addErrorMessage( 'Error: Book name cannot left empty' )

    # take book name from user and execute all validation.
    thisBookNameStr = bookNameStrTest.executeAllValidation()

    # flag to tell if this book already exist.
    bookAlreadyExistFlag = 0

    # if this book already exist
    for book in bookStore.bookStorage.bookList:
        if book.bookNameStr == thisBookNameStr:

            # get all information about this book
            thisBookPricePerDayFloat = book.bookPricePerDayFloat
            thisBookFineRateFloat = book.bookFineRateFloat
            
            # change flag to tell that this book already exist.
            bookAlreadyExistFlag = 1
            break
    
    # if this book already exist, use the old information, no need to take further input from user.
    if bookAlreadyExistFlag == 0:

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
    
    # print all available book in our store to user with index.
    bookCountInt = 0
    allBookIdList = []
    for book in bookStore.bookStorage.bookList:

        # book that has been rent and not return cannot be removed.
        if book.availableStatus == True:
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

    # get all available book but combine the same name.
    uniqueBookNameList = []
    bookCountInt = 0
    for book in bookStore.bookStorage.bookList:
        if book.bookNameStr not in uniqueBookNameList:
            uniqueBookNameList.append( book.bookNameStr )

            # print it to user.
            print( f'{ bookCountInt + 1 }. Book name: { book.bookNameStr }' )
            bookCountInt += 1
    

    # get check if user input a positive integer
    rentBookIndexTest = TestValidInput()
    rentBookIndexTest.addInputText( 'Book to be rent: ' )
    rentBookIndexTest.addValidationFunction( allowOnlyPositiveInt )
    rentBookIndexTest.addErrorMessage( 'Error: input must be only positive int' )

    # check if this book exist in out store
    rentBookIndexTest.addValidationFunction( checkIntInRange, [1, bookCountInt] )
    rentBookIndexTest.addErrorMessage( 'Error: this book does not exist.' )
    rentBookIndexStr = rentBookIndexTest.executeAllValidation()

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

    # get book name
    thisBookNameStr = uniqueBookNameList[ int( rentBookIndexStr ) - 1 ]
    thisBookIdInt = bookStore.bookStorage.getTheFirstFoundBookIdFromBookName( thisBookNameStr )

    bookStore.rentRecordStorage.rentBook( renterName, datetime.strptime(rentDate, '%Y-%m-%d'), 
    datetime.strptime(expectedReturnDate, '%Y-%m-%d'), thisBookIdInt, bookStore.bookStorage, bookStore.rentRecordStorage )
    print( 'Rent successfully.' )
    printAllRentRecord()
    state = 'start'

def returnBook():
    ''' Return a book to our store.
    '''
    global bookStore, state

    # rent record index counter
    rentRecordCountInt = 0

    # store unreturned rent record id in list
    unReturnedRentRecordIdList = [] 

    # loop to get each rent record object.
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:

        #if this rent record has not been returned then print it and keep it id.
        if rentRecord.actualReturnDate == None:
            thisBookObject = fineBookObjectById( bookStore, rentRecord.rentedBookIdInt )
            unReturnedRentRecordIdList.append( rentRecord.rentRecordIdInt )
            print( f'{ rentRecordCountInt + 1 }. Renter Name: { rentRecord.renterNameStr } Book Name: { thisBookObject.bookNameStr } Rent Date: { rentRecord.rentDate } Expected Return Date: { rentRecord.expectedReturnDate } Actual   return date: { rentRecord.actualReturnDate } Total Revenue: { rentRecord.thisRentRevenueFloat } Rent Id: { rentRecord.rentRecordIdInt }' )
            rentRecordCountInt += 1

    # if found some rent record
    if unReturnedRentRecordIdList != []:

        # get rent index to be return and validate it format and existence.
        rentIndexToBeReturnedTest = TestValidInput()
        rentIndexToBeReturnedTest.addInputText( 'Rent to return: ' )
        rentIndexToBeReturnedTest.addValidationFunction( allowOnlyPositiveInt )
        rentIndexToBeReturnedTest.addErrorMessage( 'Error: input must be only positive int' )

        # check if this record exist in out store
        rentIndexToBeReturnedTest.addValidationFunction( checkIntInRange, [1, rentRecordCountInt] )
        rentIndexToBeReturnedTest.addErrorMessage( 'Error: this record does not exist.' )
        rentIndexToBeReturnInt = rentIndexToBeReturnedTest.executeAllValidation()

        # find rent record object that user want to return.
        rentRecordObject = findRecordObjectById( bookStore, unReturnedRentRecordIdList[ int( rentIndexToBeReturnInt ) - 1 ] )

        # get rent date of that record.
        rentDate = rentRecordObject.rentDate

        # get actual return date and validate it format and time of return.
        actualReturnDateTest = TestValidInput()

        # check actual return date format
        actualReturnDateTest.addInputText( '(YYYY-M-D)Actual return Date:' )
        actualReturnDateTest.addValidationFunction( checkValidDateFormat )
        actualReturnDateTest.addErrorMessage( 'Error: incorrect date.' )

        # check if expected return date is in the future compared to rent date.
        actualReturnDateTest.addValidationFunction( checkLaterDate, [ str( rentDate ).split( ' ' )[ 0 ] ] )
        actualReturnDateTest.addErrorMessage( 'Error: actual return date must be in the future.' )
        actualReturnDate = actualReturnDateTest.executeAllValidation()
        
        # return book to our store to calculate fine, rent price and revenue.
        bookStore.rentRecordStorage.returnBook( datetime.strptime(actualReturnDate, '%Y-%m-%d'), unReturnedRentRecordIdList[ int( rentRecordCountInt ) - 1 ], bookStore.bookStorage )
        print( 'Return successfully.' )
        printAllRentRecord()
        state = 'start'
    
    # if no rent record was found.
    else:
        print( 'There is no rent record at this time.' )
        state = 'start'

def viewTotalRevenueInDateRange():
    ''' view total revenue in our store between specific date range.
    '''
    
    global bookStore, state

    # get and validate start date
    startDateTest = TestValidInput()
    startDateTest.addInputText( '(YYYY-M-D)Start Date:' )
    startDateTest.addValidationFunction( checkValidDateFormat )
    startDateTest.addErrorMessage( 'Error: incorrect date.' )
    startDate = startDateTest.executeAllValidation()

    # get end date and validate it format and time of end date.
    endDateTest = TestValidInput()

    # check actual return date format
    endDateTest.addInputText( '(YYYY-M-D)Actual return Date:' )
    endDateTest.addValidationFunction( checkValidDateFormat )
    endDateTest.addErrorMessage( 'Error: incorrect date.' )

    # check if expected return date is in the future compared to rent date.
    endDateTest.addValidationFunction( checkLaterDate, [ startDate ] )
    endDateTest.addErrorMessage( 'Error: End date must be in the future.' )
    endDate = endDateTest.executeAllValidation()

    # calculate revenue within this date range.
    revenueInThisDateRange = bookStore.calculateTotalRevenueInDateRange( datetime.strptime(startDate, '%Y-%m-%d'), datetime.strptime(endDate, '%Y-%m-%d') )
    
    # print revenue to user.
    print( f'Total Revenue in this date range is: {revenueInThisDateRange}' )
    state = 'start'

def viewTheMostPopularBook():
    ''' Show record of each book and it number of rent time starting from the most popular one.
    '''

    global bookStore, state

    # get book name and it number of rent time.
    bookNameList, bookNumberOfRentList = bookStore.viewTheMostPopularBook()

    # print result to user.
    popularityNumberInt = 1
    for bookIndex in range( len( bookNameList ) ):
        print( f'{ popularityNumberInt }. Book name: { bookNameList[ bookIndex ] }, Number of rent times: { bookNumberOfRentList[ bookIndex ] }' )
        popularityNumberInt += 1
    print( '\n' )
    state = 'start'


# main loop
def main():
    # create bookStore object
    bookStore = BookStore()


    # mock adding book to store
    bookStore.bookStorage.addBook( 'book1', float( 10 ), float( 1.5 ),
        bookStore.bookStorage )
    bookStore.bookStorage.addBook( 'book2', float( 15 ), float( 1.5 ),
        bookStore.bookStorage )
    bookStore.bookStorage.addBook( 'book3', float( 20 ), float( 1.5 ),
        bookStore.bookStorage )

    # initial state, show available options.
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

        # wait for user command.
        elif state == 'waitStartInput':
            state = input( 'Your command is: ' )
            if state not in [ '1', '2', '3', '4', '5', '6']:
                print( 'Incorrect Choice.' )
                state = 'waitStartInput'
        
        # adding book.
        elif state == '1':
            addBook()
        
        # removing book.
        elif state == '2':
            removeBook()

        # renting book.
        elif state == '3':
            rentBook()

        # returning book.
        elif state == '4':
            returnBook()

        # viewing total revenue in specific date range.
        elif state == '5':
            viewTotalRevenueInDateRange()

        # viewing the most popular book.
        elif state == '6':
            viewTheMostPopularBook()

if __name__ == '__main__':
    main()