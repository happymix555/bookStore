from RentRecord import RentRecord
from datetime import date

class RentRecordStorage:
    ''' This class used for storing and manipulating RentRecord object.
    '''

    def __init__( self ):

        # create list to store RentRecord object.
        self.rentRecordList = []

    def addNewRentRecordToStorage( self, rentRecord: RentRecord ):
        ''' This function is used to add a new rent record object to rent record storage.

            ARGS: rent record object
        '''

        # use assertion to check type of input
        assert isinstance( rentRecord, RentRecord ), 'rentRecord must be type RentRecord but got {}[{}]'.format( rentRecord, type( rentRecord ) )

        # add new rent record object to rent record storage.
        self.rentRecordList.append( rentRecord )
        
    # TODO: use this function in rent code.
    def createRentRecord( self, renterNameStr: str, rentDate: date, expectedReturnDate: date,
    rentedBookIdInt: int):
        ''' create rent record to store information about this rent.

            ARGS: renter name, rent date, expected return date, id of book to be rent, BookStorage object, RentRecordObject
        '''

        # use assertion to check type of input
        assert isinstance( renterNameStr, str ), 'renterNameStr must be type str but got {}[{}]'.format( renterNameStr, type( renterNameStr ) )
        assert isinstance( rentDate, date ), 'rentDate must be type date but got {}[{}]'.format( rentDate, type( rentDate ) )
        assert isinstance( expectedReturnDate, date ), 'expectedReturnDate must be type date but got {}[{}]'.format( expectedReturnDate, type( expectedReturnDate ) )
        assert isinstance( rentedBookIdInt, int ), 'rentedBookIdInt must be type int but got {}[{}]'.format( rentedBookIdInt, type( rentedBookIdInt ) )

        # get current available id of rent record.
        rentRecordIdInt = len( self.rentRecordList )
        
        # create a new rent record.
        thisRentRecord = RentRecord( renterNameStr, rentDate, expectedReturnDate, 
        rentedBookIdInt, rentRecordIdInt)

        # add a new rent record to storage list.
        self.rentRecordList.append( thisRentRecord )

    def calculateRentPrice( self, rentRecordIdInt: int, bookRentPricePerDayFloat: float ):
        ''' This function is used to calculate rent price and update it in a specific rent record.

            ARGS: rent record id, book fine rate per day
        '''

        # use assertion to check type of input
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )
        assert isinstance( bookRentPricePerDayFloat, float ), 'bookRentPricePerDayFloat must be type float but got {}[{}]'.format( bookRentPricePerDayFloat, type( bookRentPricePerDayFloat ) )

        # get this rent record object
        thisRentRecord = self.findRecordObjectById( rentRecordIdInt )

        # get rent date
        thisRentDate = thisRentRecord.rentDate

        # get actual return date
        thisActualReturnDate = thisRentRecord.actualReturnDate

        # time of rent
        numberOfDayRentedInDay = (thisActualReturnDate - thisRentDate).days

        # calculate rent price
        thisRentRecord.totalRentPrice = numberOfDayRentedInDay * bookRentPricePerDayFloat

    def calculateFine( self, rentRecordIdInt: int, bookFineRateFloat: int, bookRentPricePerDayFloat: int ):
        ''' This function is used for calculate fine, if any, and update it in this rent record.

            ARGS: rent record id, book fine rate, book rent price per day
        '''

        # use assertion to check type of input
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )
        assert isinstance( bookFineRateFloat, float ), 'bookFineRateFloat must be type float but got {}[{}]'.format( bookFineRateFloat, type( bookFineRateFloat ) )
        assert isinstance( bookRentPricePerDayFloat, float ), 'bookRentPricePerDayFloat must be type float but got {}[{}]'.format( bookRentPricePerDayFloat, type( bookRentPricePerDayFloat ) )

        # get this rent record object
        thisRentRecord = self.findRecordObjectById( rentRecordIdInt )

        # get actual return date
        thisActualReturnDate = thisRentRecord.actualReturnDate

        # get expected return date
        thisExpectedReturnDate = thisRentRecord.expectedReturnDate

        # get late return date in day
        thisLateReturnInDay = ( thisActualReturnDate - thisExpectedReturnDate ).days

        # if return book in time, there is no fine
        thisRentRecord.totalFine = 0.0

        # if return book late, calculate the fine
        if thisLateReturnInDay >= 0:
            thisRentRecord.totalFine = thisLateReturnInDay * bookRentPricePerDayFloat * bookFineRateFloat

    def calculateTotalRevenue( self, rentRecordIdInt: int ):
        ''' This function is used for calculate total revenue( rent price + fine ) of this rent record.

            ARGS: rent record id
        '''

        # use assertion to check type of input
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )

        # get this rent record object
        thisRentRecord = self.findRecordObjectById( rentRecordIdInt )

        # get rent price
        thisRentPrice = thisRentRecord.totalRentPrice

        # get fine 
        thisFine = thisRentRecord.totalFine

        # calculate total revenue
        thisRentRecord.thisRentRevenueFloat = thisRentPrice + thisFine


    def changeRentRecordStatusToReturned( self, rentRecordIdInt: int, actualReturnDate: date ):
        ''' change status of rent record when user return a book.
            this return status of record is derived from actual return date,
            if actual return date is not None, then this record is returned.

            ARGS: rent record id, actual return date
        '''

        # use assertion to check type of input
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )
        assert isinstance( actualReturnDate, date ), 'actualReturnDate must be type date but got {}[{}]'.format( actualReturnDate, type( actualReturnDate ) )
        
        # get this record object
        thisRentRecord = self.findRecordObjectById( rentRecordIdInt )

        # store actual return date to this rent record actual return date
        thisRentRecord.actualReturnDate = actualReturnDate


    def findRecordObjectById( self, rentRecordIdInt: int ):
        ''' find rent record object by its id.

            ARGS: rent record id

            RETURN: RentRecord object
        '''

        # use assertion to check type of input
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )

        for rentRecord in self.rentRecordList:
            if rentRecord.rentRecordIdInt == rentRecordIdInt:
                return rentRecord

