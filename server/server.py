from multiprocessing import Process
from multiprocessing import Pool
import argparse
import time
import math
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--command',help='command to be computed')
parser.add_argument('--is_parllel',help='boolean that determines the type of processing to take place')
args = vars(parser.parse_args())

print(args)

if args['is_parllel']=='false':
    print("Running: ",args['command'])
    subprocess.run([args['command']],shell=True)
else:
    with Pool() as pool:
        result = pool.map(0,args['command']) #where 0 is, put job queue where the command in the second argument will process


