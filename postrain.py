import re
import json
import argparse
import itertools

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('TRAININGFILE')
    parser.add_argument('MODELFILE')
    parser.add_argument('-h')
    args = parser.parse_args()

    tfile = open(args.TRAININGFILE)
    mfile = open(args.MODELFILE, 'w')

    #if args.h:
    #    dfile = open(args.h)

    sentences = (line.split() for line in tfile)
    traindata = (generate_examples(sentence) for sentence in sentences)
    examples = itertools.chain.from_iterable(traindata)
    
    #call perceptrain on the examples

    map(write_train_data, 
    for sentence in sentences:
    traindata = [()]


    

if __name__ == '__main__':
    main()
