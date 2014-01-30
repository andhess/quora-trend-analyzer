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
            prompt = '\nWould you like to use ' + node.name + ' ( Type: ' + node.type + ';  Sensitive:  ' + str( node.restricted ) + ') in the analysis? (yes/no)'
            details = self.getTestStats( i )
            print prompt
            print details
            result = self.makePrompt( allowedResponses, 'Please answer yes or no' )
            if not result:
                remove.append( i )

        print remove

    def getTestStats( self, columnIndex ):
        """Gets a specific data column and calculates some stats to help user determine if that row is worthwhile"""

        column = self.data[:,columnIndex]
        count = 0
        for x in column:
            if x == '':
                count += 1

        ratio = 1.0 * count len( column )
        randomEnties = []

        # grab some randoms if the column isn't blank
        if ratio <= 0.80:
            for i in range( 5 ):
                temp = ''
                while temp is not '':
                    temp = column[ rand.randrange( 0, len( column ) ) ]
                randomEnties.append( temp )


        output = 'There are ' + str( len( column ) ) + ' entries'
        output += '\nNumber of blank entries:  ' + str( count ) '  =  ' + str( 100 * ratio ) + '%'
        if randomEnties:
            output += '\nSome sample entries:  ' + str( randomEnties )[1:-1]


        # numerical analysis
        if self.headers[columnIndex].typ == 'CONT':

            for i in range( len( column ) ):
                if column[i] == '':
                    column[i] = 0
            column = column.astype('float32')

            # some stats


        # literary analysis
        if self.headers[columnIndex].typ == 'ID' or self.headers[columnIndex].typ == 'CAT':

            # most recurring entries

            # number of unique entries

            # most recurring words

            # number of unique words


        return output


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
        output = 'Name:\t\t' + self.name + '\n'
        output += 'Type:\t\t' + self.type + '\n'
        output += 'Restricted:\t' + str( self.restricted ) + '\n'

        return output



