import re
import json
import argparse
import itertools
import perceplearn

# TODO: if time permits, should adapt this in case of words with slashes in them (found in ner data)
# change all ...[1] to ...[-1]
# change all ...[0] to ...[:-1]
def generate_examples(sentence):
    wordtags = [token.split('/') for token in sentence]

    if len(wordtags) == 1:
        return [wordtags[0][1] + ' prev: curr:' + wordtags[0][0] + ' next:']

    first = wordtags[0][1] + ' prev: curr:'+ wordtags[0][0] + ' next:' + wordtags[1][0]
    last = wordtags[-1][1] + ' prev:' + wordtags[-2][0] + ' curr:' + wordtags[-1][0] + ' next:'

    examples = [wordtags[i][1] + ' prev:' + wordtags[i-1][0] + ' curr:' + wordtags[i][0] + ' next:' + wordtags[i+1][0] for i in range(1,len(wordtags)-1)]
    examples.insert(0,first)
    examples.append(last)

    return examples

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
    
    weights, vocab = perceplearn.percep_train(20, examples)
    json.dump((weights, vocab), mfile)

if __name__ == '__main__':
    main()
