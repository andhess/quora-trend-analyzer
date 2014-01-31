import csv

class csvExport:

    def __init__( self, data, headers ):
        """
        A manager to export any reorganized data to a csv file
        """
        print 'File will be exported the exports/ directory. Please enter a file name:\n'
        self.filename = raw_input.lower()

        self.exportToCSV()




    def prepareHeaders( self, arrayOfHeaders ):
        pass

    def prepareBody( self, data ):
        pass

    def exportToCSV( self, filename ):
        pass