from RentRecord import RentRecord
from datetime import date

class RentRecordStorage:
    ''' This class used for storing all RentRecord object.
    '''

    def __init__( self ):

        # create list to store RentRecord object.
        self.rentRecordList = []
        
    def rentBook( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int, bookStorageObject, rentRecordStorageObject ):
        ''' renting book

            ARGS: renter name, rent date, expected return date, id of book to be rent, BookStorage object, RentRecordObject
        '''

        # create a new rent record.
        thisRentRecord = RentRecord( renterNameStr, rentDate, expectedReturnDate, 
        rentedBookIdInt, rentRecordStorageObject )

        # add a new rent record to storage list.
        self.rentRecordList.append( thisRentRecord )

        # loop get each book in book storage
        for book in bookStorageObject.bookList:

            # if book is to be rent
            if book.bookIdInt == rentedBookIdInt:

                # correct number of rent
                book.numberOfRent += 1

                # change status to unavailable
                book.availableStatus = False

    def returnBook( self, actualReturnDate, rentRecordIdInt, bookStorageObject ):
        ''' returning book.

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

