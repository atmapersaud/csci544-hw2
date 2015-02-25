import json
import argparse
import itertools
import perceplearn

def generate_examples(sentence):
    wordtags = [token.split('/') for token in sentence]
    
    if len(wordtags) == 1:
        return []

    wordtags[0][-1] + ' prev:' + 

    first = <>
    last = <>
    examples = <>
    examples.insert(0, first)
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

    sentences = (line.split() for line in tfile)
    traindata = (generate_examples(sentence) for sentence in sentences)
    examples = itertools.chain.from_iterable(traindata)
    
    weights, vocab = perceplearn.percep_train(20, examples)
    json.dump((weights, vocab), mfile)
    

if __name__ == '__main__':
    main()
