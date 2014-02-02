import sys
import datetime
import math
import gc
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
    files = [ [ 'initial-parse', query.headers, query.data ] ]
    gc.collect()

    while True:

        job = command( responses )

        if job == 'sortr':
            sorts = sortr.


        elif job == 'export':
            writer = exp.csvExport( filename )
            for batch in files:
                writer.writeCSV( batch[0], batch[1], batch[2] )

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


if __name__ == "__main__":
    main( sys.argv[1] )