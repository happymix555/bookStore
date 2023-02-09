from datetime import datetime

DateFormatStr = '%Y-%m-%d'

class UserInput:
    ''' This class is used to take user input and validate it,
        before returning it for later usage.
    '''

    def __init__( self, outputTextForUser: str ) -> None:
        '''
        '''

        # use assertion to verify type of each input
        assert isinstance( outputTextForUser, str ), 'outputTextForUser must be type str but got {}[{}]'.format( outputTextForUser, type( inputTestForUser ) )

        self.outputTextForUser = outputTextForUser

        # to be override from sub class
        self._additionalValidationFuncToArgsDict = {}

        # cast user input to type intended to be used
        self.castTypeFunc = str

        # create list to store all the error messages
        self.errorMessageList = []

    def setAdditionalValidationFuncToArgsDict( self, validationFunc, validationArgsDict ):
        '''
        '''
        assert callable( validationFunc )
        assert isinstance( validationArgsDict, dict )

        self._additionalValidationFuncToArgsDict[ validationFunc ] = validationArgsDict

    def validation( self, userInputValue ):
        ''' For override in each subclass

            ARGS: user input string

            RETURN: list of error message
        '''

        # if have additional validation, then validate it.
        for validationFunc, validationArgsDict in self._additionalValidationFuncToArgsDict.items():
            self.errorMessageList.append( validationFunc( userInputValue, **validationArgsDict ) )

        # return all error message from validation.
        return self.errorMessageList

    def getInputAndRunValidationLoopUntilAllPassed( self ):
        ''' This function will run all validation function against input,
            if input not pass the validation, get the input and run all the validation again.
        
            RETURN: user input if pass all the  validation.
        '''

        # loop till all validation passed
        while True:

            # get input from user
            userInput = input( self.outputTextForUser )
            
            # reset error message after take input from user.
            self.errorMessageList = []

            # get all error message, if any, from all validation function
            errorMessageList = self.validation( userInput )

            # if found error, print it and get input from user again
            if errorMessageList:
                print( errorMessageList )
            else:

                # if no error was found return user input in casted type.
                return self.castTypeFunc( userInput )

class UserInputText( UserInput ):
    ''' This class is used to check if user input a string.
    '''

    def __init__ ( self, outputTextForUser: str ):
        '''
        '''
        super().__init__( outputTextForUser )

    def validation( self, userInputValue ):
        ''' validate user input value
            - check string must not be empty    
            
            ARGS: user input string

            RETURN: list of error message
        '''
        
        # call each validation function and get the error message if any.
        # if user input is not a string
        if not isinstance( userInputValue, str ):
            self.errorMessageList.append( 'Error: Text must only be a string.' )

        # if user input an empty string
        if not self.isStringNotEmpty( userInputValue ):
            self.errorMessageList.append( 'Error: Cannot put an empty string in this field.' )

        # return all the error message found.
        return self.errorMessageList

    def isStringNotEmpty( self, inputStr: str ):
        '''This function is used to check that user not input an empty string.
            
            ARGS: input string
        
            RETURN: 
                - if input pass the validation return True and error message = None
                - if input not pass the validation return False and some error message
        '''

        # if string is empty return False.
        if inputStr.strip() == '':
            return False
        
        # if string is not empty return True.
        return True

class UserInputPositiveInt( UserInput ):
    ''' This class is used to check if user input a positive integer.
    '''

    def __init__( self, outputTextForUser: str ):
        '''
        '''

        super().__init__( outputTextForUser ) 
    
        # cast user input to be int
        self.castTypeFunc = int

    def validation(self, userInputValue):
        ''' This class is used to perform the following validation
                - check if input is positive int.

            ARGS: user input string

            RETURN: list of error message
        '''

        # call validation function to validate input.
        if not self.isPositiveInt( userInputValue ):
            self.errorMessageList.append( 'Error: Only positive integer is allowed.' )

        # return error message list
        return self.errorMessageList

    def isPositiveInt( self, inputInt: str ):
        ''' This function is used to check if user input a positive integer.
        '''

        try:

            # if input is a positive int.
            if int( inputInt ) >= 0:
                return True
            else:

                # if input is a negative int.
                return False
        except:

            # if input is not an int at all.
            return False

class UserInputPositiveIntInRange( UserInputPositiveInt ):
    ''' This class is used to check user input to be a positive int in a specific range.
    '''

    def __init__( self, outputTextForUser: str, lowerBound: int, upperBound: int ):
        '''
        '''

        # user assertion to check type of input
        assert isinstance( lowerBound, int ), 'lowerBound must be type int but got {}[{}]'.format( lowerBound, type( lowerBound ) )
        assert isinstance( upperBound, int ), 'upperBound must be type int but got {}[{}]'.format( upperBound, type( upperBound ) )
        
        self.lowerBound = lowerBound
        self.upperBound = upperBound

        super().__init__( outputTextForUser )

        # cast user input from str to int
        self.castTypeFunc = int
    
    def validation( self, userInputValue: str ):
        ''' validate
                - user input a positive int between specific range.

            ARGS: user input string

            RETURN: list of error message
        '''

        # combine error message of this class with error message from additional validation function, if any
        super( UserInputPositiveIntInRange, self ).validation( userInputValue )

        # call validation and store its error, if any
        if not self.isPositiveIntInRange( userInputValue, self.lowerBound, self.upperBound ):
            self.errorMessageList.append( 'Error: Input must be a positive integer between {} to {}'.format( self.lowerBound, self.upperBound ) )
            
        return self.errorMessageList

    def isPositiveIntInRange( self, inputInt: str, lowerBound: int, upperBound: int ):
        ''' check if user input is in this range

            ARGS: user input, lower bound , upper bound
        '''

        # if input in range
        try:
            if lowerBound <= int(inputInt) <= upperBound:
                return True
            else:

                # if input not in range
                return False
        except: 
            return False

class UserInputPositiveFloat( UserInput ):
    ''' This class is used to check if user input a positive float.
    '''

    def __init__( self, outputTextForUser: str ):
        '''
        '''

        super().__init__( outputTextForUser )

        # cast user input type to float
        self.castTypeFunc = float

    def validation( self, userInputStr: str ):
        ''' Validate
                - user input a positive float

            ARGS: user input string

            RETURN: list of error message
        '''

        # call validation function and store its error message, if any
        if not self.isPositiveFloat( userInputStr ):
            self.errorMessageList.append( 'Error: This field must be only positive float.' )

        # combine error message of this class with error message from additional validation function, if any
        self.errorMessageList.extend( super( UserInputPositiveFloat, self ).validation( userInputStr ) )

        return self.errorMessageList

    def isPositiveFloat( self, userInput: str ):
        ''' check if user input a positive number( float or int).

            ARGS: user input
        '''

        # if user input is positive float
        try:
            if isinstance( float( userInput ), float ) and float( userInput ) >= 0:
                return True
            else:

                # if user input is negative float
                return False
        except:

            # if user input is not a float at all.
            return False

class UserInputDate( UserInput ):
    ''' This class is used to check user input to comply with our date string format.
    '''

    def __init__( self, outputTextForUser: str ):
        '''
        '''

        super().__init__( outputTextForUser )

        # cast user input type to float
        self.castTypeFunc = self.castStrToDateObj

    def castStrToDateObj( self, inputStr: str ):
        return datetime.strptime( inputStr, DateFormatStr )

    def validation( self, userInputStr: str ):
        ''' Validate
                - user input a date in the correct format

            ARGS: user input string

            RETURN: list of error message
        '''

        # call validation function and store its error message, if any
        if not self.isDateStrFormatCorrect( userInputStr ):
            self.errorMessageList.append( 'Error: Invalid date format.' )

        # combine error message of this class with error message from additional validation function, if any
        super( UserInputDate, self ).validation( userInputStr )

        return self.errorMessageList

    def isDateStrFormatCorrect( self, userInputStr: str ):
        ''' check if user input date with correct format.
            format is YYYY-MM-DD

            ARGS: user input
        '''

        # try to to use strptime function to cast string date to datetime object
        try:
            datetime.strptime( userInputStr, DateFormatStr )

        # if failed, it will raise value error
        except ValueError:
            return False

        # else return True
        return True
    
class UserInputDateInTheFuture( UserInputDate ):
    ''' This class is used to check date input from user to be in the future,
        compared to a reference date.
    '''

    def __init__( self, outputTextForUser: str, referenceDate: datetime ):
        '''
        '''

        super().__init__( outputTextForUser )

        self.referenceDate = referenceDate

        # cast user input type to float
        self.castTypeFunc = self.castStrToDateObj

    def castStrToDateObj( self, inputStr: str ):
        return datetime.strptime( inputStr, DateFormatStr )

    def validation( self, userInputStr: str ):
        ''' Validate
                - user input a date in the future

            ARGS: user input string

            RETURN: list of error message
        '''

        # combine error message of this class with error message from additional validation function, if any
        super( UserInputDateInTheFuture, self ).validation( userInputStr )

        # call validation function and store its error message, if any
        if not self.isDateInTheFuture( userInputStr, self.referenceDate ):
            self.errorMessageList.append( 'Error: This date must be in the future compared to {}'.format( self.referenceDate ) )

        return self.errorMessageList
    
    def isDateInTheFuture( self, userInputDateStr: str, referenceDate: datetime ):
        ''' check if user input date is in the future compared to a reference date.

            ARGS: reference date, user input date that should be in the future.
        '''

        # convert string to datetime datatype.
        try:
            userInputDateObj = datetime.strptime( userInputDateStr, DateFormatStr )

            if userInputDateObj.day - referenceDate.day >= 1:
                return True
            else:
                return False
        except: 
            return False



# for testing this class
if __name__ == '__main__':

    # mockUserInputPositiveIntValidation = UserInputPositiveInt( 'Please input a positive int: ' )
    # mockUserInputPositiveInt = mockUserInputPositiveIntValidation.getInputAndRunValidationLoopUntilAllPassed()


    # mockUserInputPositiveIntInRangeValidation = UserInputPositiveIntInRange( 'Please input a positive int in range 1 to 9: ', 1, 9 )
    # mockUserInputPositiveIntInRange = mockUserInputPositiveIntInRangeValidation.getInputAndRunValidationLoopUntilAllPassed()
    # print( mockUserInputPositiveIntInRange )

    # mockUserInputPositiveFloatValidation = UserInputPositiveFloat( 'Please input a positive float: ' )
    # mockUserInputPositiveFloat = mockUserInputPositiveFloatValidation.getInputAndRunValidationLoopUntilAllPassed()
    # print( mockUserInputPositiveFloat )

    # mockUserInputDateStrValidation = UserInputDate( 'Please input a date: ' )
    # mockUserInputDateStr = mockUserInputDateStrValidation.getInputAndRunValidationLoopUntilAllPassed()
    # print( mockUserInputDateStr )

    mockUserInputDateInTheFutureValidation = UserInputDateInTheFuture( 'Please input a date in the future: ', datetime(2023, 2, 3) )
    mockUserInputDateInTheFuture = mockUserInputDateInTheFutureValidation.getInputAndRunValidationLoopUntilAllPassed()
    print( mockUserInputDateInTheFuture )
