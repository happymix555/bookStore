from BookStorage import BookStorage
from RentRecordStorage import RentRecordStorage

from datetime import date

class BookStore:
    ''' this class used to storing BookStorage and RentRecord.
    '''

    def __init__( self ) -> None:

        # create BookStorage object
        self.bookStorage = BookStorage()

        # create RentRecord object
        self.rentRecordStorage = RentRecordStorage()

    def rentBook( self ):
        ''' This function used to rent a book.
            
            - update available status of a book.
            - create rent record to store information about this rent
            - increase number of rent of a book.
        '''
        pass

    def returnBook( self ):
        ''' This function used when user want to return a book.
            
            - change rent record status when user return a book.
        '''
        pass


    def calculateTotalRevenueInDateRange( self, startDate: date, endDate: date ):
        ''' calculate total revenue between specify date.

            ARGS: start date, end date

            RETURN: total revenue in this date range.
        '''
        assert isinstance( startDate, date )
        assert isinstance( endDate, date )

        thisTotalRevenue = 0

        # get all rent record in storage.
        for record in self.rentRecordStorage.rentRecordList:

            # if this record is closed( user already return the book. ).
            if record.actualReturnDate == None:
                continue
            # check if record occur between the specify date.
            if ( record.rentDate - startDate ).days >= 0 and ( endDate - record.actualReturnDate ).days >= 0:

                # sum the total revenue
                thisTotalRevenue += record.thisRentRevenueFloat
        
        # return total revenue as the result
        return thisTotalRevenue

    def viewTheMostPopularBook( self ):
        ''' generate the most popular book along with its number of rent time
        '''

        # create list to record book and its number of rent time.
        allBookList = []
        allNumberOfRentList = []

        bookNameStrToNumberOfRentDict = {}

        # loop get all book in storage
        for book in self.bookStorage.bookList:
            numberOfRent = bookNameStrToNumberOfRentDict.get( book.bookNameStr )
            if numberOfRent is None:
                bookNameStrToNumberOfRentDict[ book.bookNameStr ] = book.numberOfRent
            else:
                bookNameStrToNumberOfRentDict[ book.bookNameStr ] += book.numberOfRent

            # numberOfRent = bookNameStrToNumberOfRentDict.setdefault( book.bookNameStr, 0 )
            # numberOfRent += book.numberOfRent

            # # if this book is not in this record
            # if book.bookNameStr not in allBookList:

            #     # add this book and its number of rent time to the record
            #     allBookList.append( book.bookNameStr )
            #     allNumberOfRentList.append( book.numberOfRent )

            # # if book with the same name already in the record
            # else:

            #     # get index of book with the same name in the record.
            #     thisBookIndex = allBookList.index( book.bookNameStr )

            #     # increase number of rent time of this book.
            #     allNumberOfRentList[ thisBookIndex ] += book.numberOfRent

        # sorting to get the most popular book list
        theMostPopularBookNameList = []
        theMostPopularBookNumberOfRentList = []
        theMostPopularBookNumberOfRentList, theMostPopularBookNameList = zip(*sorted(zip(allNumberOfRentList, allBookList)))
        theMostPopularBookNumberOfRentList = list(theMostPopularBookNumberOfRentList)
        theMostPopularBookNumberOfRentList.reverse()
        theMostPopularBookNameList = list(theMostPopularBookNameList)
        theMostPopularBookNameList.reverse()

        # return the result
        return theMostPopularBookNameList, theMostPopularBookNumberOfRentList