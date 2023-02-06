from Book import Book
    
class BookStorage:

    def __init__( self ) -> None:
        self.bookList = []

    def addBook( self, bookNameStr: str, bookPricePerDayFloat: float, bookFineRateFloat: float, 
    bookStorageObject):
        thisBookObject = Book( bookNameStr, bookPricePerDayFloat, bookFineRateFloat, bookStorageObject)
        self.bookList.append(thisBookObject)

    def removeBook( self, bookIdInt: int ):
        for book in self.bookList:
            if book.bookIdInt == bookIdInt:
                self.bookList.remove(book)

    
