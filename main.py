import sys
import datetime
import math
#import scipy.stats
from read import parse


def main( filePath ):
    test = parse.fileParse( filePath )
    test.readQuoraData()
    print test



if __name__ == "__main__":
    main( sys.argv[1] )