To run perceplearn.py, do `python3 perceplearn.py <trainfile> <modelfile>` . In it I've implemented an averaged perceptron learning algorithm.

To run percepclassify.py, do `cat <testfile> | python3 percepclassify.py <modelfile>`. The output is written to the console, so please redirect this to a file if you desire.

My postagging and ner code both use perceplearn.py and percepclassify.py as modules in order to perform the underlying learning and classification.

#### 1. Accuracy of part-of-speech tagger:
When testing on the POS development dataset, I obtained an accuracy of **96.2%**

#### 2. Named Entity Recognizer

| Entity Type          | Precision | Recall | F-Score |
| -----------          | --------- | ------ | ------- |
| LOC (Location)       |     0.757 |  0.611 |   0.676 |
| MISC (Miscellaneous) |     0.581 |  0.508 |   0.542 |
| ORG (Organization)   |     0.712 |  0.714 |   0.713 |
| PER (Person)         |     0.773 |  0.845 |   0.807 |

##### Overall F-Score: 0.716735

#### 3. What happens if you use Naive Bayes classifier instead of perceptron classifier?
The performance suffers greatly across the board. This is explained by the Naive Bayes assumption. In this setting, the conditional independence assumption does not hold up whatsoever because the POS tags and NER tags of nearby words have a large effect on the POS tag and NER tag of any particular word.
