import sys
import os
cwd = os.getcwd()

sys.path.append(cwd)

from generate_list import printIt
for i in range(100):
    print i+1
    printIt()