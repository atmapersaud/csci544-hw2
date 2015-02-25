### 1. Accuracy of part-of-speech tagger:
When testing on the POS development dataset, I obtained an accuracy of 93.2%

### 2. Named Entity Recognizer

#### LOC

##### Precision:
##### Recall:
##### F-Score:

#### MISC

##### Precision:
##### Recall:
##### F-Score:

#### ORG

##### Precision:
##### Recall:
##### F-Score:

#### PER

##### Precision:
##### Recall:
##### F-Score:

#### Overall F-Score:

### 3. What happens if you use Naive Bayes classifier instead of perceptron classifier?
The performance suffers greatly across the board. This is explained by the Naive Bayes assumption. In this setting, the conditional independence assumption does not hold up whatsoever because the POS tags and NER tags of nearby words have a large effect on the POS tag and NER tag of any particular word.
