import os
import re
import sys
import json
import codecs
import argparse
import itertools

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import percepclassify

def generate_examples(sentence, lower, upper, digit, other):
    wt = [token.split('/') for token in sentence]
    shapes = [lower.sub('a',upper.sub('A',digit.sub('9',other.sub('-','/'.join(wt[i][:-1]))))) for i in range(len(wt))]
    if len(wt) == 1:
        return ['prev: curr:' + '/'.join(wt[0][:-1]) + ' next: prevtag: tag:' + wt[0][-1] + ' pfx3:' + '/'.join(wt[0][:-1])[:3] + ' sfx3:' + '/'.join(wt[0][:-1])[-3:] + ' sfx2:' + '/'.join(wt[0][:-1])[-2:] + ' pshape: shape:' + shapes[0]]
    first = 'prev: curr:' + '/'.join(wt[0][:-1]) + ' next:' + '/'.join(wt[1][:-1]) + ' prevtag: tag:' + wt[0][-1] + ' pfx3:' + '/'.join(wt[0][:-1])[:3] + ' sfx3:' + '/'.join(wt[0][:-1])[-3:] + ' sfx2:' + '/'.join(wt[0][:-1])[-2:] + ' pshape: shape:' + shapes[0]
    last = 'prev:' + '/'.join(wt[-2][:-1]) + ' curr:' + '/'.join(wt[-1][:-1]) + ' next: prevtag:' + wt[-2][-1] + ' tag:' + wt[-1][-1] + ' pfx3:' + '/'.join(wt[-1][:-1])[:3] + ' sfx3:' + '/'.join(wt[-1][:-1])[-3:] + ' sfx2:' + '/'.join(wt[-1][:-1])[-2:] + ' pshape:' + shapes[-2] + ' shape:' + shapes[-1]
    examples = ['prev:' + '/'.join(wt[i-1][:-1]) + ' curr:' + '/'.join(wt[i][:-1]) + ' next:' + '/'.join(wt[i+1][:-1]) + ' prevtag:' + wt[i-1][-1]  + ' tag:' + wt[i][-1] + ' pfx3:' + '/'.join(wt[i][:-1])[:3] + ' sfx3:' + '/'.join(wt[i][:-1])[-3:] + ' sfx2:' + '/'.join(wt[i][:-1])[-2:] + ' pshape:' + shapes[i-1] + ' shape:' + shapes[i] for i in range(1,len(wt)-1)]
    examples.insert(0, first)
    examples.append(last)
    return examples

#def generate_examples(sentence):
#    wordtags = [token.split('/') for token in sentence]
#    if len(wordtags) == 1:
#        return ['prev: curr:' + wordtags[0][0] + ' next: tag:' + wordtags[0][1]]
#    first = 'prev: curr:' + wordtags[0][0] + ' next:' + wordtags[1][0] + ' tag:' + wordtags[0][1]
#    last = 'prev:' + wordtags[-2][0] + ' curr:' + wordtags[-1][0] + ' next: tag:' + wordtags[-1][1]
#    examples = ['prev:' + wordtags[i-1][0] + ' curr:' + wordtags[i][0] + ' next:' + wordtags[i+1][0] + ' tag:' + wordtags[i][1] for i in range(1,len(sentence)-1)]
#    examples.insert(0,first)
#    examples.append(last)
#    return examples

def make_prediction(vdict, weights, words):
    windex = [vdict[word] if word in vdict else -1 for word in words]
    pred = percepclassify.classify(weights, windex)
    return words[1][5:], words[4][4:], pred # word, pos tag, and ner tag

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('MODELFILE')
    args = parser.parse_args()
    
    mfile = open(args.MODELFILE)
    weights, vocab = json.load(mfile)
    vdict = {vocab[i] : i for i in range(len(vocab))}
    
    #sys.stdin = codecs.getreader('latin-1')(sys.stdin.detach())
    sys.stdin = codecs.getreader('latin-1')(sys.stdin.detach())

    lower = re.compile(r'[a-z]+')
    upper = re.compile(r'[A-Z]+')
    digit = re.compile(r'[0-9]+')
    other = re.compile(r'[^a-zA-Z0-9]+')

#    for line in sys.stdin:
#        testdata = generate_examples(line.split(), lower, upper, digit, other)
#        wordpreds = [make_prediction(vdict, weights, example.split()) for example in testdata]
#        outtokens = ['/'.join(triple) for triple in wordpreds]
#        output = ' '.join(outtokens)
#        print(output)

    for line in sys.stdin:
        testdata = generate_examples(line.split(), lower, upper, digit, other)
        prevner = ''
        outtokens = []
        for example in testdata:
            ex_with_prevner = example + ' prevner:' + prevner
            wordpred = make_prediction(vdict, weights, ex_with_prevner.split())
            prevner = wordpred[2]
            outtokens.append('/'.join(wordpred))
        print(' '.join(outtokens))            

if __name__ == '__main__':
    main()
