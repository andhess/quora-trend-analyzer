import csv
import numpy as np

class fileParse:

    def __init__( self, filePath ):
        """fileParse takes in the file path for a csv file and prepares it for analysis"""

        self.headers = []
        self.data = []
        self.dataLength = 0
        self.filepath = filePath

    def __str__( self ):
        """print statement for fileParse class"""

        output = ''
        output = 'File location:  ' + self.filepath + '\n'
        output += 'Headers:\n'
        output += 'Length:  '  + str( len( self.headers) ) + '\n\n'
        for header in self.headers:
                output += str( header )
        output += '\nNumber of lines:  ' + str( self.dataLength )
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
                self.data = np.genfromtxt( csvfile, dtype = str, delimiter = ',' )

        # make sure Name row and Type row have same number of entries
        nameLength = len( names )
        if nameLength != len( types ):
            raise Exception('Number of columns is inconsistent with defined types')

        # create header objects
        for i in range( nameLength ):
            self.headers.append( headerNode( names[i], types[i] ) )

        # update row count
        self.dataLength = self.data.size

        self.setupHeaders()



    def setupHeaders( self ):
        """Procedure to ask questions to console to help narrow down the data set"""

        allowedResponses = { 'yes' : True, 'y' : True, 'ye' : True, 'no' : False, 'n' : False }

        # stores the index of columns to discard
        remove = []

        # ask console for each column
        for i, node in enumerate( self.headers ):
            prompt = '\nWould you like to use ' + node.name + ' ( Type: ' + node.type + ';  Sensitive:  ' + str( node.restricted ) + ') in the analysis? (yes/no)'
            #details = getTestStats( i )
            print prompt
            #print details
            result = self.makePrompt( allowedResponses, 'Please answer yes or no' )
            if not result:
                remove.append( i )

        print remove

    def getTestStats( self, columnIndex ):
        """Collects a little bit of data from a specific data column to help user determine if that row is worthwhile"""
        pass


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



