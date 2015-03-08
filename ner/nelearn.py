import os
import re
import sys
import json
import argparse
import itertools

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import perceplearn

def generate_examples(sentence, lower, upper, digit, other):
    wt = [token.split('/') for token in sentence]
    shapes = [lower.sub('a',upper.sub('A',digit.sub('9',other.sub('-','/'.join(wt[i][:-2]))))) for i in range(len(wt))]
    if len(wt) == 1:
        return [wt[0][-1] + ' prev: curr:' + '/'.join(wt[0][:-2]) + ' next: prevtag: tag:' + wt[0][-2] + ' pfx3:' + '/'.join(wt[0][:-2])[:3] +' sfx3:' + '/'.join(wt[0][:-2])[-3:] + ' sfx2:' + '/'.join(wt[0][:-2])[-2:] + ' pshape: shape:' + shapes[0] + ' prevner:']
    first = wt[0][-1] + ' prev: curr:' + '/'.join(wt[0][:-2]) + ' next:' + '/'.join(wt[1][:-2]) + ' prevtag: tag:' + wt[0][-2] + ' pfx3:' + '/'.join(wt[0][:-2])[:3] + ' sfx3:' + '/'.join(wt[0][:-2])[-3:] + ' sfx2:' + '/'.join(wt[0][:-2])[-2:] + ' pshape: shape:' + shapes[0] + ' prevner:'
    last = wt[-1][-1] + ' prev:' + '/'.join(wt[-2][:-2]) + ' curr:' + '/'.join(wt[-1][:-2]) + ' next: prevtag:' + wt[-2][-2] + ' tag:' + wt[-1][-2] + ' pfx3:' + '/'.join(wt[-1][:-2])[:3] + ' sfx3:' + '/'.join(wt[-1][:-2])[-3:] + ' sfx2:' + '/'.join(wt[-1][:-2])[-2:] + ' pshape:' + shapes[-2] + ' shape:' + shapes[-1] + ' prevner:' + wt[-2][-1]
    examples = [wt[i][-1] + ' prev:' + '/'.join(wt[i-1][:-2]) + ' curr:' + '/'.join(wt[i][:-2]) + ' next:' + '/'.join(wt[i+1][:-2]) + ' prevtag:' + wt[i-1][-2]  + ' tag:' + wt[i][-2] + ' pfx3:' + '/'.join(wt[i][:-2])[:3] + ' sfx3:' + '/'.join(wt[i][:-2])[-3:] + ' sfx2:' + '/'.join(wt[i][:-2])[-2:] + ' pshape:' + shapes[i-1] + ' shape:' + shapes[i] + ' prevner:' + wt[i-1][-1] for i in range(1,len(wt)-1)]
    examples.insert(0, first)
    examples.append(last)
    return examples

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('TRAININGFILE')
    parser.add_argument('MODELFILE')
    parser.add_argument('-h')
    args = parser.parse_args()

    tfile = open(args.TRAININGFILE, encoding='latin-1')
    mfile = open(args.MODELFILE, 'w')

    lower = re.compile(r'[a-z]+')
    upper = re.compile(r'[A-Z]+')
    digit = re.compile(r'[0-9]+')
    other = re.compile(r'[^a-zA-Z0-9]+')

    sentences = (line.split() for line in tfile)
    traindata = (generate_examples(sentence, lower, upper, digit, other) for sentence in sentences)
    examples = itertools.chain.from_iterable(traindata)
    
    weights, vocab = perceplearn.percep_train(20, examples)
    json.dump((weights, vocab), mfile)
    
if __name__ == '__main__':
    main()
