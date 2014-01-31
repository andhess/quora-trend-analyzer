import sys
import datetime
import math
import gc
#import scipy.stats
from read import parse


def main( filePath ):
    query = parse.fileParse( filePath )
    query.readQuoraData()
    gc.collect()
    print query

if __name__ == "__main__":
    main( sys.argv[1] )