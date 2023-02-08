from datetime import date

class RentRecord: 
    ''' This class is used to store information about the renting.
    '''
    
    def __init__( self, renterNameStr: str, rentDateObj: date, expectedReturnDate: date,
    rentedBookIdInt: int, rentRecordIdInt: int ) -> None:
        ''' Initialize RentRecord object

            ARGS: name of renter, rent date, expected return date, book id to be rent, rent record id.
        '''

        # use assertion to check type of input
        assert isinstance( renterNameStr, str ), 'renterNameStr must be type str but got {}[{}]'.format( renterNameStr, type( renterNameStr ) )
        assert isinstance( rentDateObj, date ), 'rentDate must be type date got {}[{}]'.format( rentDate, type( rentDate ) )
        assert isinstance( expectedReturnDate, date ), 'expectedReturnDate must be type date but got {}[{}]'.format( expectedReturnDate, type( expectedReturnDate ) )
        assert isinstance( rentedBookIdInt, int ), 'rentedBookIdInt must be type int but got {}[{}]'.format( rentedBookIdInt, type( rentedBookIdInt ) )
        assert isinstance( rentRecordIdInt, int ), 'rentRecordIdInt must be type int but got {}[{}]'.format( rentRecordIdInt, type( rentRecordIdInt ) )

        self.renterNameStr = renterNameStr
        self.rentDate = rentDateObj
        self.expectedReturnDate = expectedReturnDate
        self.rentedBookIdInt = rentedBookIdInt
        self.rentRecordIdInt = rentRecordIdInt
        self.totalRentPrice = None
        self.actualReturnDate = None
        self.totalFine = None
        self.thisRentRevenueFloat = None



