import sys
import datetime
import math
import gc
import re
import numpy as np
#import scipy.stats
from read import parse
from sortr import sortr
from csvOut import csvOutput as exp



def main( filePath ):

    responses = ([ 'export', 'exit', 'sort'])

    query = parse.fileParse( filePath )
    query.readQuoraData()
    print query
    files = [ [ 'initial-parse', query.data ] ]
    gc.collect()

    while True:

        job = command( responses )

        if job == 'sortr':
            name = fileNameQuery()
            sortTrial = sortr.sortr( name, query.headers, query.data )
            sortTrial.rearrangeData()
            files.append( [name, sortTrial.data] )

        elif job == 'export':
            writer = exp.csvExport( filename )
            for batch in files:
                writer.writeCSV( batch[0], query.headers, batch[1] )

        elif job == 'exit':
            sys.exit()

        else:
            pass

        gc.collect()

def command( responses ):

    log = '\nPlease select an option from the list below:\n'
    for item in responses:
        log += item + '\n'

    print log

    while True:
        choice = raw_input().lower()
        if choice in responses:
            return choice
        else:
            print 'Please select an option from the list above'


def fileNameQuery():
    print '\nPlease select a name for the file:\n'
    
    while True:
        selection = raw_input().lower()
        if re.match( "^[A-Za-z0-9_-]*$", selection ):
            return selection
        else:
            print 'Please use only valid filename characters!\n'


if __name__ == "__main__":
    main( sys.argv[1] )




