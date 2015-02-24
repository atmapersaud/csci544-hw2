## Instructions/relevant info about solution to parts I,II,III

## Any external sources

## Questions:

### 1. Accuracy of part-of-speech tagger:
When testing on SPAM development dataset, I obtained an accuracy of 99% (This seemed perhaps a bit too high, maybe overfitting was going on.)

### 2. Named Entity Recognizer

#### For each type:

##### Precision:

##### Recall:

##### F-Score:

#### Overall F-Score: (I think this is the same as accuracy)

### 3. What happens if you use Naive Bayes classifier instead of perceptron classifier?

#### report performance metrics
The performance suffers greatly across the board. This is explained by the Naive Bayes assumption. In this setting, the conditional independence assumption does not hold up whatsoever because the POS tags and NER tags of nearby words have a large effect on the POS tag and NER tag of any particular word.
