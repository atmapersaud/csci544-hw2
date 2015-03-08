import os
import re
import sys
import json
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import percepclassify

def generate_examples(sentence, lower, upper, digit, other):
    shapes = [lower.sub('a',upper.sub('A',digit.sub('9',other.sub('-',word)))) for word in sentence]

    if len(sentence) == 1:
        return ['prev: curr:' + sentence[0] + ' next: sfx3:' + sentence[0][-3:] + ' sfx2:' + sentence[0][-2:] + ' shape:' + shapes[0]]
    first = 'prev: curr:' + sentence[0] + ' next:' + sentence[1] + ' sfx3:' + sentence[0][-3:] + ' sfx2:' + sentence[0][-2:] + ' shape:' + shapes[0]
    last = 'prev:' + sentence[-2] + ' curr:' + sentence[-1] + ' next: sfx3:' + sentence[-1][-3:] + ' sfx2:' + sentence[-1][-2:] + ' shape:' + shapes[-1]
    examples = ['prev:' + sentence[i-1] + ' curr:' + sentence[i] + ' next:' + sentence[i+1] + ' sfx3:' + sentence[i][-3:] + ' sfx2:' + sentence[i][-2:] + ' shape:' + shapes[i] for i in range(1,len(sentence)-1)]
    examples.insert(0,first)
    examples.append(last)
    return examples

def make_prediction(vdict, weights, words):
    windex = [vdict[word] if word in vdict else -1 for word in words]
    pred = percepclassify.classify(weights, windex)
    return words[1][5:], pred #strip the "curr:" off of the beginning

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('MODELFILE')
    args = parser.parse_args()

    mfile = open(args.MODELFILE)
    weights, vocab = json.load(mfile)
    vdict = {vocab[i] : i for i in range(len(vocab))}

    lower = re.compile(r'[a-z]+')
    upper = re.compile(r'[A-Z]+')
    digit = re.compile(r'[0-9]+')
    other = re.compile(r'[^a-zA-Z0-9]+')
    
    for line in sys.stdin:
        testdata = generate_examples(line.split(), lower, upper, digit, other)
        wordpreds = [make_prediction(vdict, weights, example.split()) for example in testdata]
        outtokens = ['/'.join(pair) for pair in wordpreds]
        output = ' '.join(outtokens)
        print(output)
           
if __name__ == '__main__':
    main()
