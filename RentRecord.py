from Book import Book
from BookStorage import BookStorage
# from RentRecordStorage import RentRecordStorage

from datetime import date

class RentRecord: 
    ''' This class is used to store information about the renting.
    '''
    
    def __init__( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int, rentRecordStorageObject ) -> None:
        ''' Initialize RentRecord object

            ARGS: name of renter, rent date, expected return date, book id to be rent, BookStorage object, RentRecord object.
        '''
        self.renterNameStr = renterNameStr
        self.rentDate = rentDate
        self.expectedReturnDate = expectedReturnDate
        self.rentedBookIdInt = rentedBookIdInt
        self.bookRentPricePerDayFloat = None
        self.bookFineRateFloat = None
        self.totalRentPrice = None
        self.rentRecordIdInt = len( rentRecordStorageObject.rentRecordList )
        self.actualReturnDate = None
        self.totalFine = None
        self.thisRentRevenueFloat = None
    

    def calculateRentPrice( self, bookStorageObject ):
        ''' calculate rent price.

            ARGS: BookStorage object.
        '''
        # get all book in list.
        bookList = bookStorageObject.bookList

        # loop to get all Book object.
        for book in bookList:

            # if book id == id store in this record, calculate rent price.
            if book.bookIdInt == self.rentedBookIdInt:
                numberOfDayRentedInDate = self.actualReturnDate - self.rentDate
                numberOfDayRentedInDay = numberOfDayRentedInDate.days
                self.totalRentPrice = numberOfDayRentedInDay * self.bookRentPricePerDayFloat
                

    def calculateFine( self, actualReturnDate, bookStorageObject ):
        ''' Calculate rent fine if user return book late.

            ARGS: actual return date, BookStorage object
        '''

        # loop get each book.
        for book in bookStorageObject.bookList:

            # if book id == id store in this record, get fine rate of this book
            if book.bookIdInt == self.rentedBookIdInt:
                self.bookFineRateFloat = book.bookFineRateFloat
                self.bookRentPricePerDayFloat = book.bookPricePerDayFloat
                break

        # get actual return date
        self.actualReturnDate = actualReturnDate

        # get late return in day
        lateReturnInDate = self.actualReturnDate - self.expectedReturnDate
        lateReturnInDay = lateReturnInDate.days

        # if return book in time, there is no fine
        self.totalFine = 0.0

        # if return book late, calculate the fine
        if lateReturnInDay >= 0:
            self.totalFine = lateReturnInDay * self.bookRentPricePerDayFloat * self.bookFineRateFloat

    def calculateRevenue( self ):
        ''' calculate total revenue of each rent from rent record.
        '''

        self.thisRentRevenueFloat = self.totalRentPrice + self.totalFine



