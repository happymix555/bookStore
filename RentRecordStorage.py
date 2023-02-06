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
        for book in bookStorageObject:
            if book.bookIdInt == rentedBookIdInt:
                book.numberOfRent += 1

    def returnBook( self, actualReturnDate, rentRecordIdInt, bookStorageObject ):
        for record in self.rentRecordList:
            if record.rentRecordIdInt == rentRecordIdInt:
                for book in self.bookStorageObject:
                    if book.bookIdInt == record.rentBookIdInt:
                        book.availableStatus = True
                        record.calculateFine( actualReturnDate )
                        record.calculateRevenue()
                        break

