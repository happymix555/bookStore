class Book:

    def __init__( self, bookNameStr: str, bookPricePerDayFloat: float, bookFineRateFloat: float
    bookStorageObject ) -> None:
        self.bookNameStr = bookNameStr
        self.bookPricePerDayFloat = bookPricePerDayFloat
        self.bookFineRateFloat = bookFineRateFloat
        self.numberOfRent = 0
        self.availableStatus = True
        self.bookIdInt = len(bookStorageObject.bookList)