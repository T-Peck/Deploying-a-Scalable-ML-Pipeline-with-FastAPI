# Model Card


## Model Details
Tanner Peck created the model. It is logistic regression using the default hyperparameters in scikit-learn.

## Intended Use
The model is intended for classification purposes to determine if an individual makes above or below a $50,000 salary based on a multitude of demographics. This model can be used to identify which demographics or occupations contribute the most to salary inequalities.

## Training Data
The data used for training was the census.csv dataset. It contains 32562 rows with categories of : age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary. The categories used for training the model were: "workclass","education","marital-status","occupation", "relationship","race","sex","native-country".

## Evaluation Data
The census.csv data was split up into 25% for training and 75% for model performance. The 25% was the default value that Scikit-learn recommended.The data was processed using one hot encoding for the categorical features and a label binarizer for the labels.

## Metrics
The metrics used with this model were Precision, Recall, and F1. "Precision is a metric that gives you the proportion of true positives to the amount of total positives that the model predicts. It answers the question “Out of all the positive predictions we made, how many were true?”, Recall  focuses on how good the model is at finding all the positives. Recall is also called true positive rate and answers the question “Out of all the data points that should be predicted as true, how many did we correctly predict as true?”, and finally F1 Score is a measure that combines recall and precision. As we have seen there is a trade-off between precision and recall, F1 can therefore be used to measure how effectively our models make that trade-off." --Reference : https://www.labelf.ai/blog/what-is-accuracy-precision-recall-and-f1-score. 

The model results are as follows: Precision: 0.7099 | Recall: 0.2593 | F1: 0.3799

## Ethical Considerations
An ethical consideration is: Bias: with the test data used to train the model taken from real-world examples and data created by humans, the bias that exists in humans is transferred to the AI system because it uses the real-world data to train itself. The real-world data may not include fair scenarios for all population groups.

## Caveats and Recommendations
The model metrics show a high Precision of 0.7099 indicating that it has very good odds of predictions. However with the recall being 0.2593 the model will miss many true positives. The general rule states that an F1 score of 0.7 or higher is often considered good. Since F1 is a combination of Precision and Recall i believe this model needs addressed in improving its Recall stat to make it a better model.