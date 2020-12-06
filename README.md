# Sentiment-Analysis

Program created with sklearn to perform natural language processing on Amazon user reviews.

Raw Dataset: http://jmcauley.ucsd.edu/data/amazon/

Classifiers Used:
Linear SVM,
Decision Tree,
Naive Bayes,
Logistic Regression


## Notes

* Prep Data
  * Split data into train/test sets with a test size of 0.33

* Parametizing
  * Input parameter: review text <br />
  * Output: sentiment determined by user rating

* Vectorization
  * Performed natural language processing using bag-of-words model. <br />
  * Vectorized the text reviews based on the term frequency inverse document frequency (TfidVectorizer)

* Classification
  * Used 4 different classifiers and compared their mean accuracy and F1 score against test set

* Tuning Model
  * Tuned model using grid search to test parameter values for svm classifier









