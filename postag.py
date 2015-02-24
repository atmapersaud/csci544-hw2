import sys
import json
import argparse
import percepclassify

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('MODELFILE')
    args = parser.parse_args()

    mfile = open(args.MODELFILE)
    weights, vocab = json.load(mfile)
    
    for line in sys.stdin:
if __name__ == '__main__':
    main()
