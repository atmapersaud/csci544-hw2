import sys
import json
import codecs
import argparse
import itertools
import percepclassify

def generate_examples(sentence):
    wordtags = [token.split('/') for token in sentence]
    if len(wordtags) == 1:
        return ['prev: curr:' + wordtags[0][0] + ' next: tag:' + wordtags[0][1]]
    first = 'prev: curr:' + wordtags[0][0] + ' next:' + wordtags[1][0] + ' tag:' + wordtags[0][1]
    last = 'prev:' + wordtags[-2][0] + ' curr:' + wordtags[-1][0] + ' next: tag:' + wordtags[-1][1]
    examples = ['prev:' + wordtags[i-1][0] + ' curr:' + wordtags[i][0] + ' next:' + wordtags[i+1][0] + ' tag:' + wordtags[i][1] for i in range(1,len(sentence)-1)]
    examples.insert(0,first)
    examples.append(last)
    return examples

def make_prediction(vdict, weights, words):
    windex = [vdict[word] if word in vdict else -1 for word in words]
    pred = percepclassify.classify(weights, windex)
    return words[1][5:], words[3][4:], pred # word, pos tag, and ner tag

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('MODELFILE')
    args = parser.parse_args()
    
    mfile = open(args.MODELFILE)
    weights, vocab = json.load(mfile)
    vdict = {vocab[i] : i for i in range(len(vocab))}
    
    sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')

    for line in sys.stdin:
        testdata = generate_examples(line.split())
        wordpreds = [make_prediction(vdict, weights, example.split()) for example in testdata]
        outtokens = ['/'.join(triple) for triple in wordpreds]
        output = ' '.join(outtokens)
        print(output)

if __name__ == '__main__':
    main()
