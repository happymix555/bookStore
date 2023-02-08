from Book import Book
    
class BookStorage:
    ''' This class used for storing and manipulating Book object.
    '''

    def __init__( self ) -> None:

        # list to store book object.
        self.bookList = []

    def addBook( self, bookNameStr: str, bookPricePerDayFloat: float, bookFineRateFloat: float ):
        ''' add new book to book storage list.

            ARGS: book name, book rent price per day, book fine rate
        '''

        # user assertion to check type of input.
        assert isinstance( bookNameStr, str ), 'bookNameStr must be type str but got {}[{}]'.format( bookNameStr, type( bookNameStr ) )
        assert isinstance( bookPricePerDayFloat, float ), 'bookPricePerDayFloat must be type float but got {}[{}]'.format( bookPricePerDayFloat, type( bookPricePerDayFloat ) )
        assert isinstance( bookFineRateFloat, float ), 'bookFineRateFloat must be type float but got {}[{}]'.format( bookFineRateFloat, type( bookFineRateFloat ) )

        # get available book id.
        bookIdInt = len( self.bookList ) 

        # create new Book object.
        thisBookObject = Book( bookNameStr, bookPricePerDayFloat, bookFineRateFloat, bookIdInt )

        # add new Book Object to book storage list.
        self.bookList.append( thisBookObject )

    def removeBook( self, bookIdInt: int ):
        ''' remove book from book storage.

            ARGS: book id to be removed
        '''

        # user assertion to check type of input.
        assert isinstance( bookIdInt, int ), 'bookIdInt must be type int but got {}[{}]'.format( bookIdInt, type( bookIdInt ) )

        # loop get all book in book storage list
        for book in self.bookList:

            # if not found book with the target id.
            if book.bookIdInt != bookIdInt:
                continue

            # remove that book
            self.bookList.remove(book)
            break

    def getTheFirstFoundBookIdFromBookName( self, bookNameStr: str ):
        ''' get book id from book name, if we have multiple book
            with the same name, return the first one with available status == True found in book list.

            ARGS: book name
        '''

        # user assertion to check type of input.
        assert isinstance( bookNameStr, str ), 'bookNameStr must be type str but got {}[{}]'.format( bookNameStr, type( bookNameStr ) )

        # loop get each book object in book list.
        for book in self.bookList:

            # if book name is not what we want
            if book.bookNameStr != bookNameStr:
                continue

            # if book is not available
            if book.availableStatus != True:
                continue

            # if this book is what we want.
            return book.bookIdInt
            
    def findBookObjectById( self, bookIdInt: int ):
        ''' find Book object by its id.

            ARGS: book id in int

            RETURN: Book object
        '''

        # user assertion to check type of input.
        assert isinstance( bookIdInt, int ), 'bookIdInt must be type int but got {}[{}]'.format( bookIdInt, type( bookIdInt ) )

        for book in self.bookList:
            
            # if this book is not we want
            if book.bookIdInt != bookIdInt:

                # check another book
                continue

            # if this book is what we want, return it.
            return book
