from Book import Book
from BookStorage import BookStorage
from RentRecordStorage import RentRecordStorage

from datetime import date

class RentRecord: 
    
    def __init__( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int, bookStorageObject, rentRecordStorageObject ) -> None:
        self.renterNameStr = renterNameStr
        self.rentDate = rentDate
        self.expectedReturnDate = expectedReturnDate
        self.rentedBookIdInt = rentedBookIdInt
        self.totalRentPrice = self.calculateRentPrice( bookStorageObject )
        self.bookRentPricePerDay = None
        self.rentRecordIdInt = len( rentRecordStorageObject.rentRecordList )
        self.actualReturnDate = None
        self.totalFine = None
        self.thisRentRevenueFloat = None
        
    def calculateRentPrice( self, bookStorageObject ):
        bookList = bookStorageObject.bookList
        for book in bookList:
            if book.bookIdInt == self.rentedBookIdInt:
                self.bookRentPricePerDay = book.bookPricePerDayFloat
                numberOfDayRentedInDate = self.expectedReturnDate - self.rentDate
                numberOfDayRentedInDay = numberOfDayRentedInDate.day
                self.totalRentPrice = numberOfDayRentedInDay * self.bookRentPricePerDay
                book.availableStatus = False

    def calculateFine( self, actualReturnDate ):
        self.actualReturnDate = actualRetuneDate
        lateReturnInDate = self.actualReturnDate - self.expectedReturnDate
        lateReturnInDay = lateReturnInDate.days
        self.totalFine = lateReturnInDay * self.bookRentPricePerDay

    def calculateRevenue( self ):
        self.thisRentRevenueFloat = self.totalRentPrice + self.totalFine



if __name__ == '__main__':
    pass
    # mockBookStorage = BookStorage()
    # mockRentRecordStorage = RentRecordStorage()

    
    # mockRentRecord = RentRecord( 'happymix', (2023, 2, 1), (2023, 2, 2), (2023, 2, 3), 0,  )

