import argparse
import json

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('TRAININGFILE')
    parser.add_argument('MODELFILE')
    parser.add_argument('-h')
    args = parser.parse_args()

    tfile = open(args.TRAININGFILE)
    mfile = open(args.MODELFILE, 'w')

    vocab = list(frozenset(tfile.read().split()))
    vdict = { vocab[i] : i for i in range(len(vocab))}


    tfile.close()

    if args.h:
        dfile = open(args.h)


    for i in range(20):
        
if __name__ == '__main__':
    main()

parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max)
