import numpy as np

class sortr:

    def __init__( self, filename, headers, data ):

        self.filename = filename
        self.headers = headers
        self.data = data
        self.dataShape = dataShape
        self.sortOrder = []
        self.maxIndex = len( self.headers ) - 1


    def rearrangeData( self ):

        # Tell user what's going on
        output = '\n\n\n\n\n\n------ SortR ------\n\n'
        output += 'SortR allows you to rearrange data to find trends.\n'
        output += 'To get started, briefly review each column:\n\n'
        output += 'Headers:\nNumber of columns:  ' + str( len( self.headers ) )

        # Reprint the headers & their info
        for header in self.headers:
            output += header

        print output

        columnIndex = True

        while columnIndex and len( self.sortOrder ) <= len( self.headers )
            columnIndex = columnPrompt():

            if columnIndex:





        print 'Please select a name for this sorting:\n'



    def sortDataSegment( self, data, columnId):
        pass



    def splitDataIntoSegments( self, columnId ):
        pass



    def columnPrompt( self ):
        'Please select a column by which to sort the data:\n\n'

        while True:
            selection = raw_input().lower()

            # if want to finish
            if selection == 'exit':
                return False

            try:
                selection = int( selection )
                if selection >= 0 and selection <= self.maxIndex:
                    return selection
                else:
                    print 'Please select a columnn index between [0, ' + str( self.maxIndex ) + ']\n'
                
            except ValueError:
                print 'Please enter a valid number!\n'








