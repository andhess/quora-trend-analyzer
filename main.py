import sys
import datetime
import math
import gc
import numpy as np
#import scipy.stats
from read import parse
from analysis import sort
import csvOutput as exp



def main( filePath ):

    responses = ([ 'export', 'exit', 'sort'])

    query = parse.fileParse( filePath )
    query.readQuoraData()
    print query
    data = query.data
    headers = query.headers
    gc.collect()

    while True:

        job = command( responses )


        if job == 'export':
            print 'File will be written to the exports/ directory. Please enter a file name:\n'
            filename = raw_input().lower()
            writer = exp.csvExport( filename )
            writer.writeCSV( data, headers )

        elif job == 'exit':
            sys.exit()

        else:
            pass


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


if __name__ == "__main__":
    main( sys.argv[1] )