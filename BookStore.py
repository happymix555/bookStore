from BookStorage import BookStorage
from RentRecordStorage import RentRecordStorage
from RentRecord import RentRecord

from datetime import date

class BookStore:
    ''' this class used to storing BookStorage and RentRecord.
    '''

    def __init__( self ) -> None:

        # create BookStorage object
        self.bookStorage = BookStorage()

        # create RentRecord object
        self.rentRecordStorage = RentRecordStorage()

    def rentBook( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int):
        ''' This function used to rent a book.
            
            - create rent record to store information about this rent.
            - add this rent record to rent record storage.
            - update available status of a book.
            - increase number of rent of a book.

            ARGS: name of renter, rent date, expected return date, book id to be rent.
        '''

        # use assertion to check type of input.
        assert isinstance( renterNameStr, str ), 'renterNameStr must be type str but got {}[{}]'.format( renterNameStr, type( renterNameStr ) )
        assert isinstance( rentDate, date ), 'rentDate must be type date got {}[{}]'.format( rentDate, type( rentDate ) )
        assert isinstance( expectedReturnDate, date ), 'expectedReturnDate must be type date but got {}[{}]'.format( expectedReturnDate, type( expectedReturnDate ) )
        assert isinstance( rentedBookIdInt, int ), 'rentedBookIdInt must be type int but got {}[{}]'.format( rentedBookIdInt, type( rentedBookIdInt ) )
                
        # # get available id for this rent record.
        # rentRecordIdInt = len( self.rentRecordStorage.rentRecordList )
        
        # # create rent record to store information about this rent.
        # thisRentRecord = RentRecord( renterNameStr, rentDate, expectedReturnDate, rentedBookIdInt, rentRecordIdInt )

        # # add this rent record to rent record storage.
        # self.rentRecordStorage.addNewRentRecordToStorage( thisRentRecord )

        # create a new rent record and store in rent record storage.
        self.rentRecordStorage.createRentRecord( renterNameStr, rentDate, expectedReturnDate, rentedBookIdInt )

        # get book object by id
        thisBookObject = self.bookStorage.findBookObjectById( rentedBookIdInt )

        # update available status of a book.
        thisBookObject.availableStatus = False

        # increase number of rent of a book.
        thisBookObject.numberOfRent += 1        

    def returnBook( self, rentRecordIdInt: int, actualReturnDate: date ):
        ''' This function used when user want to return a book.
            
            - get actual return date of this rent record.
            - calculate rent price of this rent record.
            - calculate fine of this rent record.
            - calculate total revenue of this rent record.
            - change book available status back to available.

            ARGS: rent record id, actual return date
        '''

        # use assertion to check type of input.
        assert isinstance( actualReturnDate, date ), 'actualReturnDate must be type date but got {}[{}]'.format( actualReturnDate, type( actualReturnDate ) )
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )

        # get rent record object by id.
        rentRecord = self.rentRecordStorage.findRecordObjectById( rentRecordIdInt )
        
        # get book id.
        bookIdInt = rentRecord.rentedBookIdInt

        # get book object by book id.
        bookObject = self.bookStorage.findBookObjectById( bookIdInt )

        # get book fine rate.
        bookFineRateFloat = bookObject.bookFineRateFloat

        # get book rent price.
        bookRentPricePerDayFloat = bookObject.bookPricePerDayFloat

        # get actual return date of this rent record.
        rentRecord.actualReturnDate = actualReturnDate

        # calculate rent price of this rent record.
        self.rentRecordStorage.calculateRentPrice( rentRecordIdInt, bookRentPricePerDayFloat )

        # calculate fine of this rent record.
        self.rentRecordStorage.calculateFine( rentRecordIdInt, bookFineRateFloat, bookRentPricePerDayFloat)

        # calculate total revenue of this rent record.
        self.rentRecordStorage.calculateTotalRevenue( rentRecordIdInt )

        # change book available status back to available.
        bookObject.availableStatus = True


    def calculateTotalRevenueInDateRange( self, startDate: date, endDate: date ):
        ''' calculate total revenue between specify date.

            ARGS: start date, end date

            RETURN: total revenue in this date range.
        '''
        # use assertion to check type of input.
        assert isinstance( startDate, date ), 'startDate must be type date but got {}[{}]'.format( startDate, type( startDate ) )
        assert isinstance( endDate, date ), 'endDate must be type date but got {}[{}]'.format( endDate, type( endDate ) )

        thisTotalRevenue = 0

        # get all rent record in storage.
        for record in self.rentRecordStorage.rentRecordList:

            # if this record is closed( user already return the book. ).
            if record.actualReturnDate == None:
                continue

            # check if return date occur between the specify time of interest.
            if ( record.actualReturnDate - startDate ).days >= 0 and ( endDate - record.actualReturnDate ).days >= 0:

                # sum the total revenue
                thisTotalRevenue += record.thisRentRevenueFloat
        
        # return total revenue as the result
        return thisTotalRevenue

    def viewTheMostPopularBook( self ):
        ''' generate the most popular book along with its number of rent time

            RETURN: sorted dict with key = book name, value = number of rent in descending manner.
        '''

        bookNameStrToNumberOfRentDict = {}

        # loop get all book in storage
        for book in self.bookStorage.bookList:
            numberOfRent = bookNameStrToNumberOfRentDict.get( book.bookNameStr )

            # if book is not in dict.
            if numberOfRent is None:

                # add book name and number of rent time to dict
                bookNameStrToNumberOfRentDict[ book.bookNameStr ] = book.numberOfRent
            else:

                # if book is already in dict, increase number of rent time.
                bookNameStrToNumberOfRentDict[ book.bookNameStr ] += book.numberOfRent

        # TODO create variable for long code.
        # create book name and number of rent list in reverse sorted manner.
        bookNameStrToNumberOfRentList = sorted( bookNameStrToNumberOfRentDict.items(), key = lambda item: item[ 1 ], reverse = True )
        
        # sort key in dict based on its value in descending manner.
        sortedBookNameStrToNumberOfRentDict = { bookNameStr: numberOfRent for bookNameStr, numberOfRent in bookNameStrToNumberOfRentList }

        # sorted dict with key = book name, value = number of rent in descending order.
        return sortedBookNameStrToNumberOfRentDict