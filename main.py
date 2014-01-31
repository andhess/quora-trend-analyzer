import sys
import datetime
import math
import gc
import numpy as np
#import scipy.stats
from read import parse
from analysis import sort


def main( filePath ):

    responses = ([ 'export', 'exit', 'sort'])

    query = parse.fileParse( filePath )
    query.readQuoraData()
    print query
    data = query.data
    headers = query.headers
    gc.collect()

    while True:

        job = newCommand()



        if job == 'False'


        if job == 'exit'
            sys.exit()



    print 'Successfully imported all data from CSV'






if __name__ == "__main__":
    main( sys.argv[1] )