from RentRecord import RentRecord
from datetime import date

class RentRecordStorage:
    ''' This class used for storing all RentRecord object.
    '''

    def __init__( self ):

        # create list to store RentRecord object.
        self.rentRecordList = []
        
    def createRentRecord( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int):
        ''' create rent record to store information about this rent.

            ARGS: renter name, rent date, expected return date, id of book to be rent, BookStorage object, RentRecordObject
        '''

        # use assertion to check type of input
        assert isinstance( renterNameStr, str ), 'renterNameStr must be type str but got {}[{}]'.format( renterNameStr, type( renterNameStr ) )
        assert isinstance( rentDate, date ), 'rentDate must be type date but got {}[{}]'.format( rentDate, type( rentDate ) )
        assert isinstance( expectedReturnDate, date ), 'expectedReturnDate must be type date but got {}[{}]'.format( expectedReturnDate, type( expectedReturnDate ) )
        assert isinstance( rentedBookIdInt, date ), 'rentedBookIdInt must be type int but got {}[{}]'.format( rentedBookIdInt, type( rentedBookIdInt ) )

        # get current available id of rent record.
        rentRecordIdInt = len( self.rentRecordList )
        
        # create a new rent record.
        thisRentRecord = RentRecord( renterNameStr, rentDate, expectedReturnDate, 
        rentedBookIdInt, rentRecordIdInt)

        # add a new rent record to storage list.
        self.rentRecordList.append( thisRentRecord )

    def changeRentRecordStatusToReturned( self, actualReturnDate, rentRecordIdInt, bookStorageObject ):
        ''' change status of rent record when user return a book.

            ARGS: return date, rent record id, BookStorage object
        '''

        # loop get all record in rent record list
        for record in self.rentRecordList:

            # if rent record != the record to be return, do nothing
            if record.rentRecordIdInt != rentRecordIdInt:
                continue

            # if rent record == the record to be return
            # loop get each book in book storage list
            for book in bookStorageObject.bookList:

                # if book != book rented in this record, do nothing
                if book.bookIdInt != record.rentedBookIdInt:
                    continue
                
                # if book == book rented in this record, returning this book
                # change book status to available
                book.availableStatus = True
                
                # calculate fine
                record.calculateFine( actualReturnDate, bookStorageObject )

                # calculate rent price
                record.calculateRentPrice( bookStorageObject )

                # calculate revenue
                record.calculateRevenue()
                break

    def findRecordObjectById( self, rentRecordIdInt ):
        ''' find rent record object by its id.

            ARGS: rent record id

            RETURN: RentRecord object
        '''

        for rentRecord in self.rentRecordList:
            if rentRecord.rentRecordIdInt == rentRecordIdInt:
                return rentRecord

