import numpy as np

class sortr:

    def __init__( self, headers, data ):
        """An interface to sort columns in any way"""

        self.headers = headers
        self.data = data
        self.sortOrder = []
        self.maxIndex = len( self.headers ) - 1


    def rearrangeData( self ):
        """
        Instigates the sorting process.
        Makes consecutive prompts to help user determine which columns to sort by.
        """ 

        # Tell user what's going on
        output = '\n\n\n\n\n\n------ SortR ------\n\n'
        output += 'SortR allows you to rearrange data to find trends.\n'
        output += 'To get started, briefly review each column:\n\n'
        output += 'Headers:\nNumber of columns:  ' + str( len( self.headers ) )

        # Reprint the headers & their info
        for i, header in enumerate( self.headers ):
            output += '\nColumn ' + str( i ) + ':  ' + header.name

        print output

        columnIndex = 0
        print 'Select the index of the column you wish to sort by, in the order of priority'
        print 'When done selecting, type "exit"'

        # figure out which columns we want to sort by
        while columnIndex >= 0 and len( self.sortOrder ) <= len( self.headers ):
            columnIndex = self.columnPrompt()
            if columnIndex >= 0:
                self.sortOrder.append( str( columnIndex ) )

        self.sortData()

        print '\n\nSortR done\n'


    def sortData( self ):
        """
        Rearranges data so it can be sorted, sorts, then reverts to orignal format.
        Sorting is done via mergesort so that the sort is stable.
        """

        self.setupDataForSorting()
        self.data = np.sort( self.data, kind = 'mergesort' , order = self.sortOrder )
        self.unpackDataForExport()


    def setupDataForSorting( self ):
        """Converts Numpy matrix to numpy tuple matrix with dtypes"""
        
        # Numpy has some odd quirks that makes this a little ugly
        dtype = []
        for i, item in enumerate( self.headers ):
            if item.type == 'CONT':
                columnDataType = 'float32'
            else:
                columnDataType = 'S64'

            dtype.append( ( str( i ), columnDataType ) )    

        temp = []
        for row in self.data:
            temp.append( tuple( row ) )

        self.data = np.array( temp, dtype = dtype )


    def unpackDataForExport( self ):
        """Reverts Numpy tuple matrix to normal Numpy matrix"""

        tempData = []
        for row in self.data:
            tempData.append( list( row ) )

        self.data = np.array( tempData )


    def columnPrompt( self ):
        """Prompt for selecting a column"""

        print 'Please select a column by which to sort the data:'

        while True:
            selection = raw_input().lower()

            # if want to finish
            if selection == 'exit':
                return -1

            try:
                selection = int( selection )
                if selection >= 0 and selection <= self.maxIndex:
                    if self.sortOrder.count( str( selection ) ) < 1:
                        return selection
                    else:
                        print 'Already selected ' + str( selection )
                else:
                    print 'Please select a columnn index between [0, ' + str( self.maxIndex ) + ']'
                
            except ValueError:
                print 'Please enter a valid number!'






