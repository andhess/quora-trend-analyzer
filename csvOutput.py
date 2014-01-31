import os
import csv

class csvExport:

    def __init__( self, filename ):
        """A manager to export any reorganized data to a csv file"""   

        self.filename = filename


    def writeCSV( self, data, headers ):

        head = self.prepareHeaders( headers )

        # setup file to save in a directory
        script_dir = os.path.dirname( os.path.abspath( __file__ ) )
        dest_dir = os.path.join( script_dir, 'exports' )    
        try:
                os.makedirs(dest_dir)
        except OSError:
                pass # already exists

        # make a CSV of it all
        csvPath = os.path.join( dest_dir, self.filename + '.csv' )
        
        # commence writing
        writeCSV = csv.writer( open( csvPath , "wb" ) )

        # headers
        for entry in head:
            writeCSV.writerow( entry )

        # rest of data
        for row in data:
            writeCSV.writerow( row )

        print 'Successfully wrote csv file to exports/' + self.filename + '.csv'


    def prepareHeaders( self, arrayOfHeaders ):
        names = []
        types = []

        for item in arrayOfHeaders:
            names.append( item.name )
            if item.restricted:
                types.append( item.type + '/SENSITIVE' )
            else:
                types.append( item.type )

        return [ names, types ]