import json
import argparse
import datetime
import itertools

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
   
    data = [line for line in tfile]
    tfile.close()

    weights, vocab = percep_train(20,data)
    json.dump((weights, vocab), mfile)
    

def percep_train(N, data):
    """
    Trains a basic perceptron for the given dataset, and writes the results to a modelfile

    Args:
      N (int): The maximum number of iterations for training
      data (list of strings): A document list, where the first word of each document is its label
    """
    documents = [line.split() for line in data]
    classes = list(frozenset([doc[0] for doc in documents]))
    vocab = list(frozenset(list(itertools.chain.from_iterable(documents))))
    vdict = {vocab[i] : i for i in range(len(vocab))}

    weights = {classname : [0]*(len(vocab)+1) for classname in classes}

    w_avg = {classname : [0]*(len(vocab)+1) for classname in classes}

    for i in range(N):
        print('starting iteration ' + str(i) + ' at ' + str(datetime.datetime.now()))
        for doc in documents:
            windex = [vdict[word] for word in doc[1:]]

            z = classify(weights, windex)
            y = doc[0]
                        
            if z != y:
                for j in windex:
                    weights[z][j] -= 1
                    weights[y][j] += 1
                # update bias term
                weights[z][-1] -= 1
                weights[y][-1] += 1

        for classname in weights:
            w_avg[classname] = [w_avg[classname][k] + weights[classname][k] for k in range(len(vocab)+1)]
    return w_avg, vocab

def classify(w_dict, doc):
    class_scores = [(key,compute_score(w_dict[key], doc)) for key in w_dict]
    return max(class_scores, key=lambda x: x[1])[0]
    
def compute_score(w, doc):
    return w[-1] + sum([w[word] for word in doc])
    
if __name__ == '__main__':
    main()
