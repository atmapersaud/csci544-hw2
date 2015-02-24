import re
import json
import argparse
import itertools

def generate_examples(sentence):
    wordtags = [token.split('/') for token in sentence]
    first = (wordtags[0], wordtags[1])
    last = (wordtags[-2], wordtags[-1])
    triples = [(wordtags[i-1], wordtags[i], wordtags[i+1]) for i in range(1,len(wordtags)-1)]
    # could use triples.insert(0,first) and triples.append(last)
    # remember to add "prev" "curr" and "next" 

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
