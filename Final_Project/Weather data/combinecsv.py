import glob
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--d",dest="directory", type=str,
                    help="input a directory")
parser.add_argument("--v",help="input a directory using --d")
parser.add_argument("--o",dest="outputfile", type=str,
                    help="input the file name for output file")
args = parser.parse_args()
answer = args.directory
out = args.outputfile
interesting_files = glob.glob(answer+"/*.txt") 

header_saved = False
with open(out+'.csv','wb') as fout:
    for filename in interesting_files:
		#reader = csv.reader(filename)
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)
