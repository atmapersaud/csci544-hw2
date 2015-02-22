import sys
import json
import argparse

def classify(w_dict, doc):
    class_scores = [(key,compute_score(w_dict[key], doc)) for key in w_dict]
    return max(class_scores, key=lambda x: x[1])[0]
    
def compute_score(w, doc):
    return w[-1] + sum([w[word] for word in doc])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('MODELFILE')
    args = parser.parse_args()

    mfile = open(args.MODELFILE)
    weights, vocab = json.load(mfile)
    vdict = {vocab[i] : i for i in range(len(vocab))}

    for line in sys.stdin:
        windex = [vdict[word] for word in line.split() if word in vdict]
        pred = classify(weights, windex)
        print(pred)

if __name__ == '__main__':
    main()
