import json
import argparse
import itertools
import perceplearn

def generate_examples(sentence):
    wordtags = [token.split('/') for token in sentence]
    if len(wordtags) == 1:
        return [wordtags[0][-1] + 'prev: curr:' + '/'.join(wordtags[0][:-2]) + ' next: tag:' + wordtags[0][-2]]
    first = wordtags[0][-1] + ' prev: curr:' + '/'.join(wordtags[0][:-2]) + ' next:' + '/'.join(wordtags[1][:-2]) + ' tag:' + wordtags[0][-2]
    last = wordtags[-1][-1] + ' prev:' + '/'.join(wordtags[-2][:-2]) + ' curr:' + '/'.join(wordtags[-1][:-2]) + ' next: tag:' + wordtags[-1][-2]
    examples = [wordtags[i][-1] + ' prev:' + '/'.join(wordtags[i-1][:-2]) + ' curr: ' + '/'.join(wordtags[i][:-2]) + ' next:' + '/'.join(wordtags[i+1][:-2]) + ' tag:' + wordtags[i][-2] for i in range(1,len(wordtags)-1)]
    examples.insert(0, first)
    examples.append(last)
    return examples

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('TRAININGFILE')
    parser.add_argument('MODELFILE')
    parser.add_argument('-h')
    args = parser.parse_args()

    tfile = open(args.TRAININGFILE, errors='ignore')
    mfile = open(args.MODELFILE, 'w')

    sentences = (line.split() for line in tfile)
    traindata = (generate_examples(sentence) for sentence in sentences)
    examples = itertools.chain.from_iterable(traindata)
    
    weights, vocab = perceplearn.percep_train(20, examples)
    json.dump((weights, vocab), mfile)
    
if __name__ == '__main__':
    main()
