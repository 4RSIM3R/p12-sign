import os
import json
import sys

if __name__ == '__main__':
    print(json.dumps(os.system('pyhanko sign validate --pretty-print --retroactive-revinfo ' + sys.argv[1])))
