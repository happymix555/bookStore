from Book import Book
    
class BookStorage:
    ''' This class used for storing Book object.
    '''

    def __init__( self ) -> None:

        # list to store book object.
        self.bookList = []

    def addBook( self, bookNameStr: str, bookPricePerDayFloat: float, bookFineRateFloat: float ):
        ''' add new book to book storage list.

            ARGS: book name, book rent price per day, book fine rate, BookStorage object,
        '''
        assert isinstance( bookNameStr, str ), 'bookNameStr must be type str but got {}[{}]'.format( bookNameStr, type( bookNameStr ) )

        # create new Book object.
        #   TODO: change from self to book id
        thisBookObject = Book( bookNameStr, bookPricePerDayFloat, bookFineRateFloat, self )

        # add new Book Object to book storage list.
        self.bookList.append( thisBookObject )

    def removeBook( self, bookIdInt: int ):
        ''' remove book from book storage.

            ARGS: book id to be removed
        '''

        # loop get all book in book storage list
        for book in self.bookList:

            # if found book with the target id.
            if book.bookIdInt == bookIdInt:

                # remove that book
                self.bookList.remove(book)

    def getTheFirstFoundBookIdFromBookName( self, bookNameStr ):
        ''' get book id from book name, if we have multiple book
            with the same name, return the first one found in book list.

            ARGS: book name
        '''

        # loop get each book object in book list and perform the following action:
        for book in self.bookList:
            if book.bookNameStr == bookNameStr:
                return book.bookIdInt
