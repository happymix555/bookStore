from BookStorage import BookStorage
from RentRecordStorage import RentRecordStorage

from datetime import date

class BookStore:

    def __init__( self ) -> None:
        self.bookStorage = BookStorage()
        self.rentRecordStorage = RentRecordStorage()

    def calculateTotalRevenueInDateRange( self, startDate: date, endDate: date ):
        thisTotalRevenue = 0
        for record in self.rentRecordStorage:
            if record.actualReturnDate != None:
                if ( record.rentDate - startDate ).days >= 0 and ( record.endDate - record.actualReturnDate ).days >= 0:
                    thisTotalRevenue += record.thisRentRevenueFloat
        return thisTotalRevenue

    def viewTheMostPopularBook( self ):
        allBookList = []
        allNumberOfRentList = []
        for book in self.bookStorage:
            if book.bookNameStr not in allBookList:
                allBookList.append(book.bookNameStr)
                allNumberOfRentList.append(book.numberOfRent)
            else:
                thisBookIndex = allBookList.index(book.bookNameStr)
                allNumberOfRentList[thisBookIndex] += book.numberOfRent
        theMostPopularBookNameList = []
        theMostPopularBookNumberOfRentList = []
        theMostPopularBookNumberOfRentList, theMostPopularBookNameList = zip(*sorted(zip(allNumberOfRentList, allBookList)))
        return theMostPopularBookNameList, theMostPopularBookNumberOfRentList