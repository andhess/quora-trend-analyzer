import numpy as np

class column:

    def __init__( self, headers, data ):
        """
        Column is a module that helps to show relationships.
        A column of ID, or CAT can be compared against a column of CAT.
        """

        self.headers = headers
        self.maxIndex = len( headers ) - 1
        self.data = data
        self.comparison = {}


    def analyze( self ):

        # Tell user what's going on
        output = '\n\n\n\n\n\n------ Column ------\n\n'
        output += 'Column allows you to see the correlation between columns.\n'
        output += 'A column of type ID or CAT will be compared against a column of type CONT.\n'
        output += 'To get started, briefly review each column:\n\n'
        output += 'Headers:\nNumber of columns:  ' + str( len( self.headers ) ) + '\n'

        # Reprint the headers & their info
        for i, header in enumerate( self.headers ):
            output += '\nColumn ' + str( i ) + ':  ' + str( header )

        print output

        # get columns
        stringColIndex =   self.columnPrompt()
        floatColIndex  =   self.columnPrompt( 'CONT' )
        stringColumn   =   self.data[:,stringColIndex]
        floatColumn    =   self.data[:,floatColIndex]

        # loop through and populate self.comparison
        for string, number in zip( stringColumn, floatColumn ):
            if self.comparison.get( string ) is None:
                self.comparison[string] = np.array([])

            self.comparison[string] = np.append( self.comparison[string], number )

        # now collect stats on each set and set as tuple matrix
        self.data = []
        for key in self.comparison:
            col = self.comparison[key].astype('float32')
            temp = ( key, np.amin( col ), np.amax( col ), np.ptp( col ), np.mean( col ), np.median( col ), np.std( col ), np.var( col ) )
            self.data.append( temp )

        dtype = [ ('0', 'S64'), ('1', 'float32'), ('2', 'float32'), ('3', 'float32'), ('4', 'float32'), ('5', 'float32'), ('6', 'float32'), ('7', 'float32') ]
        self.data = np.array( self.data, dtype = dtype )

        # ask which column to sort by - not very practical to have tie breakers here but,
        # if column isn't Name, then Name column will be default tie breaker
        sortingCol = self.sortPrompt()
        sortBy = [ str( sortingCol ) ]
        if sortingCol != 0:
            sortBy.append( '0' )

        self.data = np.sort( self.data, kind = 'mergesort', order = sortBy )
        self.exportData()

        # redo the headers
        self.headers = [ self.headers[stringColIndex], self.headers[floatColIndex] ]


    def exportData( self ):
        """Updates self.data to standard 2D matrix"""
        data = [ [ 'Name', 'Min', 'Max', 'Range', 'Mean', 'Median', 'Standard Deviation', 'Variance'] ]
        print self.data
        print self.data[0]
        print list( self.data[0] )
        for row in self.data:
            data.append( list( row ) )

        self.data = data


    def columnPrompt( self, typ = 'CAT/ID' ):
        """Prompt for selecting a column"""

        print 'Please select the index of column of type ' + typ + ' for comparison:'

        while True: 
            try:
                selection = int( raw_input() )
                if selection >= 0 and selection <= self.maxIndex:
                    if typ.find( self.headers[selection].type ) > -1:
                        return selection
                    else:
                        print 'Please select a column of type ' + typ
                else:
                    print 'Please select a columnn index between [0, ' + str( self.maxIndex ) + ']'
                
            except ValueError:
                print 'Please enter a valid number!'


    def sortPrompt( self ):
        """Prompt for selecting a sorting column"""

        output = '\nNew columns:\n\n'
        newColumns = [ 'Name', 'Min', 'Max', 'Range', 'Mean', 'Median', 'Standard Deviation', 'Variance']
        self.maxIndex = len( newColumns ) - 1
        for k, item in enumerate( newColumns ):
            output += 'Column ' + str( k ) + ':  ' + item + '\n'

        output += '\nPlease select a column index to sort by:'

        print output

        while True: 
            try:
                selection = int( raw_input() )
                if selection >= 0 and selection <= self.maxIndex:
                    return selection
                else:
                    print 'Please select a columnn index between [0, ' + str( self.maxIndex ) + ']'
                
            except ValueError:
                print 'Please enter a valid number!'


