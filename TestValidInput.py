class TestValidInput:
    ''' This class used to implement chain of input validation in
        stage by stage manner.

        Every function that will use with this class must receive a user function as the 
        first argument.

        If function used with this class have another argument than user input,
        user must add those argument in list in the same order of the function. 
    '''

    def __init__ ( self ) -> None:

        # show this text to user to inform what to input.
        self.inputText = None

        # list to store all validation function for this input
        self.validationFunctionList = []

        # list of argument for each validation function.
        self.validationFunctionArgumentList = []

        # list to store all error message to inform user why some validation not pass
        self.errorMessageList = []


    def addInputText( self, inputText ):
        ''' add input text of this test object.
        '''
        self.inputText = inputText

    def addValidationFunction( self, validationFunction, validationFunctionArgumentList = [] ):
        ''' add validation function to list of validation function to use with this input.
            validation function should return True if pass else, return False.      
        '''

        # add validation function
        self.validationFunctionList.append( validationFunction )

        # add argument of validation function
        self.validationFunctionArgumentList.append( validationFunctionArgumentList )

    def addErrorMessage( self, errorMessage ):
        ''' add error message of each validation function to be shown to user and help them correct the input.
        '''
        self.errorMessageList.append( errorMessage )

    def executeAllValidation( self ):
        ''' execute all validation function to verify this input text from user.
        '''
        # initial state is get input from user
        state = 'getUserInput'

        # while loop to test all validation cases.
        while 1:
            
            # initial state is get input from user
            if state == 'getUserInput':

                # get input from user.
                userInput = input( self.inputText )

                #go to validation state
                state = 'validationInput'

            # this state validate input with all validation function.
            elif state == 'validationInput':
                
                # correct counter
                correctCounter = 0

                #loop get all validation function
                for validationFunctionAndMessageIndex in range( len ( self.validationFunctionList ) ):
                    thisValidationFunction = self.validationFunctionList[ validationFunctionAndMessageIndex ]
                    thisValidationFunctionArgumentList = self.validationFunctionArgumentList[ validationFunctionAndMessageIndex ]

                    # validate input according to each function
                    try:
                        if thisValidationFunctionArgumentList == []:
                            thisFunctionResult = thisValidationFunction( userInput )
                        else:
                            thisFunctionResult = thisValidationFunction( userInput, *thisValidationFunctionArgumentList )
                    
                    # if unforeseen error was found, tell the user and take the input from uses again.
                    except Exception as e:
                        print( f'Found error of a validation function: { self.validationFunctionList[ validationFunctionAndMessageIndex ] }' )
                        print( e )
                        state = 'getUserInput'
                        break

                    # if input is invalid.
                    if not thisFunctionResult:

                        # print error message of the validation function to user.
                        print( self.errorMessageList[ validationFunctionAndMessageIndex ] )

                        # go to state that take input from user again
                        state = 'getUserInput'
                        break

                    # if input pass the validation, perform another function then increase the correct counter
                    correctCounter += 1

                # if correct counter == number of validation function to test.
                if correctCounter == len( self.validationFunctionList ):
                        
                        # return user input to be used.
                        return userInput



























