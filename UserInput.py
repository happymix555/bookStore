from datetime import datetime

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
        self._validationFunctionToArgumentDict = {}


    def getInputAndRunValidationLoopUntilAllPassed( self ):
        ''' This function will run all validation function against input,
            if input not pass the validation, get the input and run all the validation again.
        
            RETURN: user input if pass all the  validation.
        '''

        # initial state = get user input
        state = 'getUserInput'

        # number of validation passed counter
        numberOfValidationPassed = 0

        # loop till input pass all the validation.
        while True:
        
            # initial state = get user input
            if state == 'getUserInput':
                    
                # take input from user
                userInput = input( self.outputTextForUser )

                # next state = validate user input
                state = 'validateUserInput'

            # validation state
            elif state == 'validateUserInput':
        
                # if no validation function was found, then not validate this input.
                # not sure if this is a good idea, but will find out another time.
                if self._validationFunctionToArgumentDict == {}:
                    return userInput
                
                # loop get each validation function
                for validationFunction, keywordToArgumentDict in self._validationFunctionToArgumentDict.items():

                    # if no validation argument
                    if keywordToArgumentDict == None:
                        validationResult, errorMessage = validationFunction( userInput )
                    else:
                        
                        # if have additional argument
                        validationResult, errorMessage = validationFunction( userInput, **keywordToArgumentDict )

                    # if not pass the test
                    if validationResult == False:
                        
                        # print Error message
                        print( errorMessage )

                        # get user input again
                        state = 'getUserInput'
                        break

                    # increase number of validation passed.
                    numberOfValidationPassed += 1

                # if pass all the test, return user input 
                if numberOfValidationPassed == len( self._validationFunctionToArgumentDict.items() ):
                    return userInput

class UserInputNotEmptyStr( UserInput ):
    ''' This class is used to check if user input a string.
    '''

    def __init__ ( self, outputTextForUser: str ):
        '''
        '''
        super().__init__( outputTextForUser )

        # add validation function and its argument to dict
        self._validationFunctionToArgumentDict[ self.isStringNotEmpty ] = None

    def isStringNotEmpty( self, inputStr: str ):
        '''This function is used to check that user not input an empty string.
            
            ARGS: input string
        
            RETURN: 
                - if input pass the validation return True and error message = None
                - if input not pass the validation return False and some error message
        '''

        # if string is empty return False.
        if inputStr.strip() == '':
            return False, 'Error: Cannot put an empty string in this field.'
        
        # if string is not empty return True.
        return True, None

class UserInputPositiveInt( UserInput ):
    ''' This class is used to check if user input a positive integer.
    '''

    def __init__( self, outputTextForUser: str ):
        '''
        '''

        super().__init__( outputTextForUser ) 
        self._validationFunctionToArgumentDict = {
            self.isPositiveInt: None,
        }

    def isPositiveInt( self, inputInt: str ):
        ''' This function is used to check if user input a positive integer.
        '''

        try:

            # if input is a positive int.
            if int( inputInt ) >= 0:
                return True, None
            else:

                # if input is a negative int.
                return False, 'Error: Only positive integer is allowed.'
        except:

            # if input is not an int at all.
            return False, 'Error: Only positive integer is allowed.'
        
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

        # add validation function and its argument to dict.
        self._validationFunctionToArgumentDict[ self.isPositiveIntInRange ] = { 'lowerBound': self.lowerBound, 'upperBound': self.upperBound }


    def isPositiveIntInRange( self, inputInt: str, lowerBound: int, upperBound: int ):
        ''' check if user input is in this range

            ARGS: user input, lower bound , upper bound
        '''

        # if input in range
        if lowerBound <= int(inputInt) <= upperBound:
            return True, None
        else:

            # if input not in range
            return False, 'Error: Input must in between {} to {}'.format( lowerBound, upperBound )
        

class UserInputPositiveFloat( UserInput ):
    ''' This class is used to check if user input a positive float.
    '''

    def __init__( self, outputTextForUser: str ):
        '''
        '''

        super().__init__( outputTextForUser )

        # add validation function and its argument to dict.
        self._validationFunctionToArgumentDict[ self.isPositiveFloat ] = None

    def isPositiveFloat( self, userInput: str ):
        ''' check if user input a positive number( float or int).

            ARGS: user input
        '''

        # if user input is positive float
        try:
            if isinstance( float( userInput ), float ) and float( userInput ) >= 0:
                return True, None
            else:

                # if user input is negative float
                return False, 'Error: This field must be only positive float.'
        except:

            # if user input is not a float at all.
            return False, 'Error: This field must be only positive float.'

class UserInputDate( UserInput ):
    ''' This class is used to check user input to comply with our date string format.
    '''

    def __init__( self, outputTextForUser: str ):
        '''
        '''

        super().__init__( outputTextForUser )

        # add validation function and its argument to dict.
        self._validationFunctionToArgumentDict[ self.isDateStrFormatCorrect ] = None

    def isDateStrFormatCorrect( self, userInputStr: str ):
        ''' check if user input date with correct format.
            format is YYYY-MM-DD

            ARGS: user input
        '''

        # try to to use strptime function to cast string date to datetime object
        try:
            datetime.strptime( userInputStr, '%Y-%m-%d' )

        # if failed, it will raise value error
        except ValueError:
            return False, 'Error: Invalid date format.'

        # else return True
        return True, None
    
class UserInputDateInTheFuture( UserInputDate ):
    ''' This class is used to check date input from user to be in the future,
        compared to a reference date.
    '''

    def __init__( self, outputTextForUser: str, referenceDate: datetime ):
        '''
        '''

        super().__init__( outputTextForUser )

        self.referenceDate = referenceDate

        # add validation function and its argument to dict.
        self._validationFunctionToArgumentDict[ self.isDateInTheFuture ] = {'referenceDate': self.referenceDate}

    def isDateInTheFuture( self, userInputDateStr: str, referenceDate: datetime ):
        ''' check if user input date is in the future compared to a reference date.

            ARGS: reference date, user input date that should be in the future.
        '''

        # convert string to datetime datatype.
        userInputDateObj = datetime.strptime(userInputDateStr, '%Y-%m-%d')

        if userInputDateObj.day - referenceDate.day >= 1:
            return True, None
        else:
            return False, 'Error: This date must be in the future compared to {}'.format( referenceDate )



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
