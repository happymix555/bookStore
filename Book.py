class Book:

    def __init__( self, bookNameStr: str, bookPricePerDayFloat: float, bookFineRateFloat: float,
    bookIdInt: int ) -> None:
        
        # use assertion to check type of input
        assert isinstance( bookNameStr, str ), 'bookNameStr must be type str but got {}[{}]'.format( bookNameStr, type( bookNameStr ) )
        assert isinstance( bookPricePerDayFloat, float ), 'bookPricePerDayFloat must be type float but got {}[{}]'.format( bookPricePerDayFloat, type( bookPricePerDayFloat ) )
        assert isinstance( bookFineRateFloat, float ), 'bookFineRateFloat must be type float but got {}[{}]'.format( bookFineRateFloat, type( bookFineRateFloat ) )
        assert isinstance( bookIdInt, int ), 'bookIdInt must be type int but got {}[{}]'.format( bookIdInt, type( bookIdInt ) )

        self.bookNameStr = bookNameStr
        self.bookPricePerDayFloat = bookPricePerDayFloat
        self.bookFineRateFloat = bookFineRateFloat
        self.numberOfRent = 0
        self.availableStatus = True
        self.bookIdInt = bookIdInt