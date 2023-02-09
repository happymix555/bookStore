from BookStore import BookStore

from datetime import datetime
from InvalidInputPrevention import *
from TestValidInput import *
from UserInput import *


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

    global bookStore
    rentRecordCountInt = 1

    # loop to get each rent record object.
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:

        #if this rent record has not been returned then print it
        if rentRecord.actualReturnDate == None:
            thisBookObject = bookStore.bookStorage.findBookObjectById( bookStore, rentRecord.rentedBookIdInt )
            print( f'{rentRecordCountInt}. Renter Name: {rentRecord.renterNameStr} Book Name: { thisBookObject.bookNameStr } Rent Date: {rentRecord.rentDate} Expected Return Date: {rentRecord.expectedReturnDate} Actual return date: {rentRecord.actualReturnDate} Total Revenue: {rentRecord.thisRentRevenueFloat} Rent Id: {rentRecord.rentRecordIdInt}' )
            rentRecordCountInt += 1
    print( '\n' )

def addBook():
    ''' Add new book to our store.
    '''

    global bookStore, state

    # create book name test object
    bookNameStrTest = UserInputText( 'Book name: ' )

    # take book name from user and execute all validation.
    thisBookNameStr = bookNameStrTest.getInputAndRunValidationLoopUntilAllPassed()

    # flag to tell if this book already exist.
    bookAlreadyExistFlag = 0

    # if this book already exist
    for book in bookStore.bookStorage.bookList:
        if book.bookNameStr != thisBookNameStr:
            continue

        # get all information about this book
        thisBookPricePerDayFloat = book.bookPricePerDayFloat
        thisBookFineRateFloat = book.bookFineRateFloat
        
        # change flag to tell that this book already exist.
        bookAlreadyExistFlag = 1
        break
    
    # if this book already exist, use the old information, no need to take further input from user.
    if bookAlreadyExistFlag == 0:

        # get rent price per day of this book through TestValidInput class.
        testBookPricePerDayFloat = UserInputPositiveFloat( 'Book rent price per Day: ' )
        
        # check if book rent price is only a positive float.
        thisBookPricePerDayFloat = testBookPricePerDayFloat.getInputAndRunValidationLoopUntilAllPassed()
        
        # get fine rate of this book through TestValidInput class.
        testBookFineRateFloat = UserInputPositiveFloat( 'Book fine rate: ' )
        
        # check if fine rate is only a positive float.
        thisBookFineRateFloat = testBookFineRateFloat.getInputAndRunValidationLoopUntilAllPassed()

    # create Book object and add it to a BookStorage in BookStore.
    bookStore.bookStorage.addBook( thisBookNameStr, thisBookPricePerDayFloat, thisBookFineRateFloat )
    
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
    bookIdToBeRemovedTest = UserInputPositiveIntInRange( 'Book to be removed: ', 1, bookCountInt )

    # check if input is in bookCountInt's range to ensure that user select only the book that
    # exist in our store.
    bookIndexToBeRemovedStr = bookIdToBeRemovedTest.getInputAndRunValidationLoopUntilAllPassed()

    bookStore.bookStorage.removeBook( int( allBookIdList[ int( bookIndexToBeRemovedStr ) - 1 ] ) )
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

        # if book available
        if book.availableStatus != True:
            continue

        if book.bookNameStr not in uniqueBookNameList:
            uniqueBookNameList.append( book.bookNameStr )

            # print it to user.
            print( f'{ bookCountInt + 1 }. Book name: { book.bookNameStr }' )
            bookCountInt += 1
    

    # get check if user input a positive integer
    rentBookIndexTest = UserInputPositiveIntInRange( 'Book to be rent: ', 1, bookCountInt )

    # check if this book exist in out store
    rentBookIndexStr = rentBookIndexTest.getInputAndRunValidationLoopUntilAllPassed()

    # get renter name
    renterNameStrTest = UserInputText( 'Renter name: ' )

    # take book name from user and execute all validation.
    renterNameStr = renterNameStrTest.getInputAndRunValidationLoopUntilAllPassed()

    # get and validate rent date
    rentDateTest = UserInputDate( '(YYYY-M-D)Rent Date: ' )
    rentDate = rentDateTest.getInputAndRunValidationLoopUntilAllPassed()

    # get and validate expected return date
    expectedReturnDateTest = UserInputDateInTheFuture( '(YYYY-M-D)Expected return Date: ', rentDate )

    # check if expected return date is in the future compared to rent date.
    expectedReturnDate = expectedReturnDateTest.getInputAndRunValidationLoopUntilAllPassed()

    # get book name
    thisBookNameStr = uniqueBookNameList[ int( rentBookIndexStr ) - 1 ]
    thisBookIdInt = bookStore.bookStorage.getTheFirstFoundBookIdFromBookName( thisBookNameStr )

    bookStore.rentBook( renterNameStr, rentDate, 
    expectedReturnDate, thisBookIdInt )
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

    # loop to get each rent record object.rentBook
    for rentRecord in bookStore.rentRecordStorage.rentRecordList:

        #if this rent record has not been returned then print it and keep it id.
        if rentRecord.actualReturnDate == None:
            thisBookObject = bookStore.bookStorage.findBookObjectById( rentRecord.rentedBookIdInt )
            unReturnedRentRecordIdList.append( rentRecord.rentRecordIdInt )
            print( f'{ rentRecordCountInt + 1 }. Renter Name: { rentRecord.renterNameStr } Book Name: { thisBookObject.bookNameStr } Rent Date: { rentRecord.rentDate } Expected Return Date: { rentRecord.expectedReturnDate } Actual   return date: { rentRecord.actualReturnDate } Total Revenue: { rentRecord.thisRentRevenueFloat } Rent Id: { rentRecord.rentRecordIdInt }' )
            rentRecordCountInt += 1

    # if found some rent record
    if unReturnedRentRecordIdList != []:

        # get rent index to be return and validate it format and existence.
        rentIndexToBeReturnedTest = UserInputPositiveIntInRange( 'Rent to return: ', 1, rentRecordCountInt )

        # check if this record exist in out store
        rentIndexToBeReturnInt = rentIndexToBeReturnedTest.getInputAndRunValidationLoopUntilAllPassed()

        # find rent record object that user want to return.
        rentRecordObject = bookStore.rentRecordStorage.findRecordObjectById( unReturnedRentRecordIdList[ rentIndexToBeReturnInt - 1 ] )

        # get rent date of that record.
        rentDate = rentRecordObject.rentDate

        # get actual return date and validate it format.
        actualReturnDateTest = UserInputDateInTheFuture( '(YYYY-M-D)Actual return Date: ', rentDate )

        # check if expected return date is in the future compared to rent date.
        actualReturnDate = actualReturnDateTest.getInputAndRunValidationLoopUntilAllPassed()
        
        # return book to our store to calculate fine, rent price and revenue.
        bookStore.returnBook( unReturnedRentRecordIdList[ rentRecordCountInt - 1 ], actualReturnDate )
        print( 'Return successfully.' )
        printAllRentRecord()
        state = 'start'
    
    # if no rent record was found.
    else:
        print( 'There is no rent record at this time.' )
        state = 'start'
    print( '\n' )

def viewTotalRevenueInDateRange():
    ''' view total revenue in our store between specific date range.
    '''
    
    global bookStore, state

    # get and validate start date
    startDateTest = UserInputDate( '(YYYY-M-D)Start Date: ' )
    startDate = startDateTest.getInputAndRunValidationLoopUntilAllPassed()

    # get end date and validate it format and time of end date.
    endDateTest = UserInputDateInTheFuture( '(YYYY-M-D)Actual return Date: ', startDate )

    # check if expected return date is in the future compared to rent date.
    endDate = endDateTest.getInputAndRunValidationLoopUntilAllPassed()

    # calculate revenue within this date range.
    revenueInThisDateRange = bookStore.calculateTotalRevenueInDateRange( startDate, endDate )
    
    # print revenue to user.
    print( f'Total Revenue in this date range is: {revenueInThisDateRange}' )
    state = 'start'

def viewTheMostPopularBook():
    ''' Show record of each book and it number of rent time starting from the most popular one.
    '''

    global bookStore, state

    # get book name and it number of rent time.
    sortedBookNameStrToNumberOfRentDict = bookStore.viewTheMostPopularBook()

    # print result to user.
    popularityNumberInt = 1
    for bookName in sortedBookNameStrToNumberOfRentDict:
        print( f'{ popularityNumberInt }. Book name: { bookName }, Number of rent times: { sortedBookNameStrToNumberOfRentDict[ bookName ] }' )
        popularityNumberInt += 1
    print( '\n' )
    state = 'start'

# TODO do not use global variable, throw it in each function called.
# main loop
def main():

    global bookStore, state

    # create bookStore object
    bookStore = BookStore()


    # mock adding book to store
    bookStore.bookStorage.addBook( 'book1', float( 10 ), float( 1.5 ) )
    bookStore.bookStorage.addBook( 'book2', float( 15 ), float( 1.5 ) )
    bookStore.bookStorage.addBook( 'book3', float( 20 ), float( 1.5 ) )

    # initial state, show available options.
    state = 'start'
    while True:
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