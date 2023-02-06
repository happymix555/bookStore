from RentRecord import RentRecord
from datetime import date

class RentRecordStorage:

    def __init__( self ):
        self.rentRecordList = []
        
    def rentBook( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int, bookStorageObject, rentRecordStorageObject ):
        thisRentRecord = RentRecord( renterNameStr, rentDate, expectedReturnDate, 
        rentedBookIdInt, bookStorageObject, rentRecordStorageObject )
        self.rentRecordList.append( thisRentRecord )
        for book in bookStorageObject.bookList:
            if book.bookIdInt == rentedBookIdInt:
                book.numberOfRent += 1
                book.availableStatus = False
                # print(book.bookNameStr)

    def returnBook( self, actualReturnDate, rentRecordIdInt, bookStorageObject ):
        # print( 'in returnBook function.' )
        for record in self.rentRecordList:
            # print( record.rentRecordIdInt )
            if record.rentRecordIdInt != rentRecordIdInt:
                continue

            for book in bookStorageObject.bookList:
                if book.bookIdInt != record.rentedBookIdInt:
                    continue

                book.availableStatus = True
                # print( record.bookRentPricePerDayFloat )
                record.calculateFine( actualReturnDate, bookStorageObject )
                record.calculateRentPrice( bookStorageObject )
                record.calculateRevenue()
                break

