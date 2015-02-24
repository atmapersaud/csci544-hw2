import sys
import json
import argparse
import percepclassify

def generate_examples(sentence):
    if len(sentence) == 1:
        return 'prev: curr:' + sentence[0] + ' next:'
    first = 'prev: curr:' + sentence[0] + ' next:' + sentence[1]
    last = 'prev:' + sentence[-2] + ' curr:' + sentence[-1] + ' next:'
    examples = ['prev:' + sentence[i-1] + ' curr:' + sentence[i] + ' next:' + sentence[i+1] for i in range(1,len(sentence)-1)]
    examples.insert(0,first)
    examples.append(last)
    return examples

def make_prediction(vdict, weights, words):
    windex = [vdict[word] if word in vdict else -1 for word in words]
    pred = percepclassify.classify(weights, windex)
    return words[1], pred

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('MODELFILE')
    args = parser.parse_args()

    mfile = open(args.MODELFILE)
    weights, vocab = json.load(mfile)
    vdict = {vocab[i] : i for i in range(len(vocab))}
    
    for line in sys.stdin:
        testdata = generate_examples(line.split())
        wordpreds = [make_prediction(vdict, weights, example.split()) for example in testdata]
        outtokens = ['/'.join(pair) for pair in wordpreds]
        output = ' '.join(outtokens)
        print(output)
           
if __name__ == '__main__':
    main()
