import os
import csv

class csvExport:

    def __init__( self ):
        """A manager to export any reorganized data to a csv file"""   

        # timestamp will be the directory where all files are stored
        self.timeStamp = datetime.datetime.now().strftime( "%H-%M-%S%f-%m-%d-%Y" )


    def writeCSV( self, filename, headers, data ):

        head = self.prepareHeaders( headers )

        # generate a unique filename with a time stamp
        timeStamp = datetime.datetime.now().strftime( "%H-%M-%S%f-%m-%d-%Y" )

        # setup file to save in a directory
        script_dir = os.path.dirname( os.path.abspath( __file__ ) )
        dest_dir = os.path.join( script_dir, '..', 'exports', timeStamp )    
        try:
                os.makedirs(dest_dir)
        except OSError:
                pass # already exists

        # make a CSV of it all
        csvPath = os.path.join( dest_dir, filename + '.csv' )
        
        # commence writing
        writeCSV = csv.writer( open( csvPath , "wb" ) )

        # headers
        for entry in head:
            writeCSV.writerow( entry )

        # rest of data
        for row in data:
            writeCSV.writerow( row )


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