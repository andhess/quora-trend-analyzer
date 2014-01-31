import csv
import numpy as np
import random as rand

class fileParse:

    def __init__( self, filePath ):
        """fileParse takes in the file path for a csv file and prepares it for analysis"""

        self.headers = []
        self.data = []
        self.dataShape = 0
        self.filepath = filePath

    def __str__( self ):
        """print statement for fileParse class"""

        output = ''
        output = 'File location:  ' + self.filepath + '\n'
        output += 'Headers:\n'
        output += 'Length:  '  + str( len( self.headers) ) + '\n\n'
        for header in self.headers:
                output += str( header )
        output += '\nDimensions of data:  ' + str( self.dataShape )
        return output

    def readQuoraData( self ):
        """
        Commences the interactive reading protocol
        Terminal prompts will help the user select the most useful data
        Headers --> self.headers
        Data    --> self.data
        """

        with open( self.filepath , 'rb' ) as csvfile:
            csvData = csv.reader( csvfile, delimiter=',' )

            # first process the 1st two lines
            names = csvData.next()
            types = csvData.next()

            # grab the rest of the data now
            for row in csvData:
                self.data.append( row )

        self.data = np.array( self.data )
        self.dataShape = self.data.shape

        # make sure Name row and Type row have same number of entries
        nameLength = len( names )
        if nameLength != len( types ):
            raise Exception('Number of columns is inconsistent with defined types')

        # create header objects
        for i in range( nameLength ):
            self.headers.append( headerNode( names[i], types[i] ) )

        self.setupHeaders()


    def setupHeaders( self ):
        """Procedure to ask questions to console to help narrow down the data set"""

        allowedResponses = { 'yes' : True, 'y' : True, 'ye' : True, 'no' : False, 'n' : False }

        # stores the index of columns to discard
        remove = []

        # ask console for each column
        for i, node in enumerate( self.headers ):
            prompt = '\nWould you like to use data from column ' + node.name + ' (Type: ' + node.type + ';  Sensitive:  ' + str( node.restricted ) + ') in the analysis? (yes/no)\n'
            details = self.getTestStats( i )
            print prompt
            print details
            result = self.makePrompt( allowedResponses, 'Please answer yes or no' )
            if not result:
                remove.append( i )

        # now delete each column from data set
        for i in reversed( remove ):
            self.data = np.delete( self.data, i, 1 )
            del self.headers[i]
        self.dataShape = self.data.shape


    def getTestStats( self, columnIndex ):
        """Gets a specific data column and calculates some stats to help user determine if that row is worthwhile"""

        column = self.data[:,columnIndex]
        count = 0
        for x in column:
            if x == '' or x == 'N/A':
                count += 1

        ratio = 1.0 * count / len( column )
        randomEnties = []

        # grab some randoms if the column isn't blank
        if ratio <= 0.80:
            for i in range( 3 ):
                temp = ''
                while temp == '':
                    temp = column[ rand.randrange( 0, len( column ) ) ]
                randomEnties.append( temp )


        output = 'There are ' + str( len( column ) ) + ' entries'
        output += '\nNumber of blank entries:  ' + str( count ) + '  =>  ' + str( 100 * ratio ) + '%'
        if randomEnties:
            output += '\nSome randomly selected sample entries:  ' + str( randomEnties )[1:-1] + '\n'


        # numerical analysis
        if self.headers[columnIndex].type == 'CONT':

            columnRemove = np.array([])

            if count > 0:

                # set null values in column to 0, duplicate all entries in columnRemove
                for i in range( len( column ) ):
                    if column[i] == '' or column[i] == 'N/A':
                        column[i] = 0
                    else:
                        column[i] = column[i].translate( None, '%-#')
                        columnRemove = np.append( columnRemove, column[i] )

                columnRemove = columnRemove.astype('float32')

            # get stats on column
            column = column.astype('float32')
            if np.any( columnRemove ):
                output += '\nSet empty values to 0'
            output += '\nMax: ' + str( np.amax( column ) ) + '  Min:  ' + str( np.amin( column ) ) + '  Range:  ' + str( np.ptp( column ) )
            output += '\nMean:  ' + str( np.mean( column ) ) + '  Meadian:  ' + str( np.median( column ) )
            output += '\nStandard Deviation:  ' + str( np.std( column ) ) + '  Variance:  ' + str( np.var( column ) )

            
            # if also have columnRemoved, get the same stats
            if np.any( columnRemove ):
                output += '\n\nSame stats but ignoring empty values'
                output += '\nMax: ' + str( np.amax( columnRemove ) ) + '  Min:  ' + str( np.amin( columnRemove ) ) + '  Range:  ' + str( np.ptp( columnRemove ) )
                output += '\nMean:  ' + str( np.mean( columnRemove ) ) + '  Meadian:  ' + str( np.median( columnRemove ) )
                output += '\nStandard Deviation:  ' + str( np.std( columnRemove ) ) + '  Variance:  ' + str( np.var( columnRemove ) )


        # literary analysis
        elif self.headers[columnIndex].type == 'CAT' or self.headers[columnIndex].type == 'ID':

            words = {}
            phrases = {}

            for entry in column:
                wordSet = entry.split()
                for word in wordSet:
                    if words.get( word ) is None:
                        words[word] = 1
                    else:
                        words[word] += 1
                if phrases.get( entry ) is None:
                    phrases[entry] = 1
                else:
                    phrases[entry] += 1

            output += '\nNumber of unique phrases:  ' + str( len( phrases ) )
            output += '\nNumber of unique words:  ' + str( len( words ) )

            if len( words ) > 2:

                # get the 3 most recurring phrases and words

                # phrases
                output += '\nThe most occuring phrases:  '
                for i in range(3):
                    maxPhrase = max( phrases, key = phrases.get )
                    output += str( maxPhrase ) + ': ' + str( phrases[maxPhrase] ) + '\t'
                    del phrases[maxPhrase]

                # words
                output += '\nThe most occuring words:  '
                for i in range(3):
                    maxWord = max( words, key = words.get )
                    output += str( maxWord ) + ': ' + str( words[maxWord] ) + '\t'
                    del words[maxWord]

            else:
                output += '\nThe most occuring phrases:  '
                for key in phrases.iterkeys():
                    output += str( key ) + ': ' + str( phrases[key] ) + '\t'

                output += '\nThe most occuring words:  '
                for key in words.iterkeys():
                    output += str( key ) + ': ' + str( words[key] ) + '\t'

        # otherwise it's TIME and not going to alter that right now
        else:
            output += '\nNo further information currently available for time categories'

        return output + '\n'


    def makePrompt( self, allowedResponses, answerTheQuestion=None,question=None ):
        """
        An order for parse to send a question to the console
        Inputs: question (string), allowedResponses (dict)
        """
        if question:
            print question
        
        # loop until a valid answer is received
        while True:
            choice = raw_input().lower()
            choice = allowedResponses.get(choice)
            if choice is not None:
                return choice
            if answerTheQuestion:
                print answerTheQuestion


class headerNode():
    """
    Object class to represent each column of data
    Attributes:
        string name, string type, bool restricted (/SENSITIVE)
    """

    def __init__( self, name, typ ):
        self.name = name
        splice = typ.find('/SENSITIVE')
        if  splice >= 0:
            self.type = typ[:splice]
            self.restricted = True
        else:
            self.type = typ
            self.restricted = False

    def __str__( self ):
        output = '\nName:\t\t' + self.name + '\n'
        output += 'Type:\t\t' + self.type + '\n'
        output += 'Restricted:\t' + str( self.restricted ) + '\n'

        return output



