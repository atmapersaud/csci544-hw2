import json
import argparse
import itertools

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('TRAININGFILE')
    parser.add_argument('MODELFILE')
    parser.add_argument('-h')
    args = parser.parse_args()

    tfile = open(args.TRAININGFILE)
    mfile = open(args.MODELFILE, 'w')
   
    # get data, class labels, and vocab
    documents = [line.split() for line in tfile]
    classes = list(frozenset([doc[0] for doc in documents]))
    vocab = list(frozenset(list(itertools.chain.from_iterable(documents))))
    vdict = { vocab[i] : i for i in range(len(vocab))}
    tfile.close()

    if args.h:
        dfile = open(args.h)

# N is number of iterations
# data is list of strings
def percep_train(N, data):
    documents = [line.split() for line in data]
    classes = list(frozenset([doc[0] for doc in documents]))
    vocab = list(frozenset(list(itertools.chain.from_iterable(documents))))
    vdict = { vocab[i] : i for i in range(len(vocab))}

    weights = { classname : [0]*len(vocab) for classname in classes}

    for i in range(N):
        for doc in documents:
            z = argmax w * f(x)
            if z != doc[0]:
                wz = wz - f(x)
                wy = wy + f(x)

if __name__ == '__main__':
    main()
