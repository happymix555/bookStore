from Book import Book
from BookStorage import BookStorage
# from RentRecordStorage import RentRecordStorage

from datetime import date

class RentRecord: 
    
    def __init__( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int, bookStorageObject, rentRecordStorageObject ) -> None:
        self.renterNameStr = renterNameStr
        self.rentDate = rentDate
        self.expectedReturnDate = expectedReturnDate
        self.rentedBookIdInt = rentedBookIdInt
        self.bookRentPricePerDayFloat = None
        self.bookFineRateFloat = None
        self.totalRentPrice = None
        # self.calculateRentPrice( bookStorageObject )
        self.rentRecordIdInt = len( rentRecordStorageObject.rentRecordList )
        self.actualReturnDate = None
        self.totalFine = None
        self.thisRentRevenueFloat = None
        
        
    def calculateRentPrice( self, bookStorageObject ):
        bookList = bookStorageObject.bookList
        for book in bookList:
            if book.bookIdInt == self.rentedBookIdInt:
                # print( 'in calculateRentPrice function.' )
                # self.bookRentPricePerDayFloat = book.bookPricePerDayFloat
                # print( self.bookRentPricePerDayFloat )
                print( book.bookPricePerDayFloat ) 
                numberOfDayRentedInDate = self.actualReturnDate - self.rentDate
                numberOfDayRentedInDay = numberOfDayRentedInDate.days
                self.totalRentPrice = numberOfDayRentedInDay * self.bookRentPricePerDayFloat
                

    def calculateFine( self, actualReturnDate, bookStorageObject ):
        # print( 'in calculateFine function' )
        for book in bookStorageObject.bookList:
            if book.bookIdInt == self.rentedBookIdInt:
                self.bookFineRateFloat = book.bookFineRateFloat
                self.bookRentPricePerDayFloat = book.bookPricePerDayFloat
                break
        self.actualReturnDate = actualReturnDate
        lateReturnInDate = self.actualReturnDate - self.expectedReturnDate
        lateReturnInDay = lateReturnInDate.days
        # print( lateReturnInDay )
        # print( self.bookRentPricePerDayFloat )
        self.totalFine = 0.0
        if lateReturnInDay >= 0:
            self.totalFine = lateReturnInDay * self.bookRentPricePerDayFloat * self.bookFineRateFloat
        # print( self.totalFine )

    def calculateRevenue( self ):
        self.thisRentRevenueFloat = self.totalRentPrice + self.totalFine



if __name__ == '__main__':
    pass
    # mockBookStorage = BookStorage()
    # mockRentRecordStorage = RentRecordStorage()

    
    # mockRentRecord = RentRecord( 'happymix', (2023, 2, 1), (2023, 2, 2), (2023, 2, 3), 0,  )

