from multiprocessing import Process
from multiprocessing import Pool
import argparse
import time
import math
import subprocess
import jobs as job

parser = argparse.ArgumentParser()
parser.add_argument('--command',help='command to be computed')
parser.add_argument('--is_parllel',help='boolean that determines the type of processing to take place')
args = vars(parser.parse_args())

print(args)


if __name__ == '__main__':
    if args['is_parllel']=='false':
        print("Running: ",args['command'])
        subprocess.run([args['command']],shell=True)
    else:
        p = Process(target=job.create_job,args=([args['command']],))
        p.start()
        p.join()


