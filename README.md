To run perceplearn.py, do `python3 perceplearn.py <trainfile> <modelfile>` . In it I've implemented an averaged perceptron learning algorithm.

To run percepclassify.py, do `cat <testfile> | python3 percepclassify.py <modelfile>`. The output is written to the console, so please redirect this to a file if you desire.

My postagging and ner code both use perceplearn.py and percepclassify.py as modules in order to perform the underlying learning and classification.

### 1. Accuracy of part-of-speech tagger:
When testing on the POS development dataset, I obtained an accuracy of 96.2%

### 2. Named Entity Recognizer

#### LOC

##### Precision: 0.756927
##### Recall: 0.610772
##### F-Score: 0.676040

#### MISC

##### Precision: 0.580977
##### Recall: 0.507865
##### F-Score: 0.541966

#### ORG

##### Precision: 0.711854
##### Recall: 0.713529
##### F-Score: 0.712691

#### PER

##### Precision: 0.772625
##### Recall: 0.845336
##### F-Score: 0.807347

#### Overall F-Score: 0.716735

### 3. What happens if you use Naive Bayes classifier instead of perceptron classifier?
The performance suffers greatly across the board. This is explained by the Naive Bayes assumption. In this setting, the conditional independence assumption does not hold up whatsoever because the POS tags and NER tags of nearby words have a large effect on the POS tag and NER tag of any particular word.