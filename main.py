from BookStore import BookStore

def addBook():
    global bookStore, state
    thisBookNameStr = input( 'Book name: ' )
    thisBookPricePerDayFloat = input( 'Book rent price per Day: ' )
    thisBookFineRateFloat = input( 'Book fine rate: ' )
    bookStore.bookStorage.addBook( thisBookNameStr, float( thisBookPricePerDayFloat ), float( thisBookFineRateFloat ),
    bookStore.bookStorage )
    for book in bookStore.bookStorage.bookList:
        print( book.bookNameStr )
        print( book.bookIdInt )
        print( '\n' )
    state = 'start'

def removeBook():
    global bookStore, state
    

#main loop

bookStore = BookStore()

state = 'start'
while 1:
    if state == 'start':
        print( 'Welcome to Yannix book store.' )
        print( 'Please select the option that you want.' )
        print( '1. Add new book.' )
        print( '2. Remove a book.' )
        print( '3. Rent a book.' )
        print( '4. Return a book.' )
        print( '5. View total revenue in date range.' )
        print( '6. View the most popular books.' )
        state = 'waitStartInput'

    elif state == 'waitStartInput':
        state = input( 'Your command is: ' )
        if state not in [ '1', '2', '3', '4', '5', '6']:
            print( 'Incorrect Choice.' )
            state = 'waitStartInput'

        
    elif state == '1':
        addBook()