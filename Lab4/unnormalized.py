'''
References
https://www.youtube.com/watch?v=G4UVJoGFAv0
http://regexlib.com/DisplayPatterns.aspx
'''

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

#results file that you store the results(0's/1's) for the test file/data
results = open("result.txt", "w+")
results.truncate(0)



#reading in the data
df1 = pd.read_table('yelp_labelled.txt', header=None)
df2 = pd.read_table('imdb_labelled.txt', header=None)
df3 = pd.read_table('amazon_cells_labelled.txt', header=None)


#Concatinating the three datasets
df = pd.concat([df1, df2, df3])

#getting the column with all the classes(0/1 pos/neg)
classes = df[1]

# convert class labels to binary values, 0 = negative/0 and 1 = positive/1
encoder = LabelEncoder()
Y = encoder.fit_transform(classes)

#storing each sentence in a list
documents = df[0]

#cleaning the data

# Replace money symbols with 'moneysymb' (£ can by typed with ALT key + 156)
processed = documents.str.replace(r'£|\$', 'moneysymb')

# Replace numbers with 'numbr'
processed = processed.str.replace(r'\d+(\.\d+)?', 'numbr')

# Remove punctuation
processed = processed.str.replace(r'[^\w\d\s]', ' ')

# Replace whitespace between terms with a single space
processed = processed.str.replace(r'\s+', ' ')

# Remove leading and trailing whitespace
processed = processed.str.replace(r'^\s+|\s+?$', '')

# converting words to lower case form
processed = processed.str.lower()

# creating a bag of words vocabulary
all_words = []

for message in processed:
    words = word_tokenize(message)
    for w in words:
        all_words.append(w)

all_words = nltk.FreqDist(all_words)


word_features = list(all_words.keys())

# The find_features function will determine which of the word features are contained in document
def find_features(docs):
    docs = str(docs)
    words = word_tokenize(docs)
    features = {}
    for word in word_features:
        features[word] = (word in words)

    return features


# Finding features for all the docs
all_docs = list(zip(processed, Y))
# print(all_docs)

# define a seed for reproducibility
seed = 1
np.random.seed = seed
np.random.shuffle(all_docs)
# calling find_features function for each sentence/document
featuresets = [(find_features(text), label) for (text, label) in all_docs]

# spliting the data into training data and test data
train_data, test_data = model_selection.train_test_split(featuresets, test_size=0.15, random_state=seed)

# print(len(train_data))
# print(len(test_data))


#creating and training the logistic regression classifier
def logistic_classifier(file):
    file=str(file)
    logistic_model = SklearnClassifier(LogisticRegression())

    # train the model on the training data
    logistic_model.train(train_data)
    accuracy = nltk.classify.accuracy(logistic_model, test_data) * 100
    print("Logistic Regression Classifier Accuracy: {}".format(accuracy))

    # Tag the test file.
    with open(file, 'r') as fin:
        for test_sentence in fin:
            # Tokenize the line.
            doc = word_tokenize(test_sentence.lower())
            featurized_doc = {i: (i in doc) for i in word_features}
            tagged_label = logistic_model.classify(featurized_doc)
            results.write(str(tagged_label)+'\n')


#creating and training the naive bayes classifier
def naive_classifier(file):
    file=str(file)
    naive_bayes_model = SklearnClassifier(MultinomialNB())

    # train the model on the training data
    naive_bayes_model.train(train_data)

    accuracy = nltk.classify.accuracy(naive_bayes_model, test_data) * 100
    print("Naive Bayes Classifier Accuracy: {}".format(accuracy))

    # Tag the test file.
    with open(file, 'r') as fin:
        for test_sentence in fin:
            # Tokenize the line.
            doc = word_tokenize(test_sentence.lower())
            featurized_doc = {i: (i in doc) for i in word_features}
            tagged_label = naive_bayes_model.classify(featurized_doc)
            results.write(str(tagged_label)+'\n')


'''
Code below is to test the accuracy of the classifiers
'''

# # and test on the testing dataset!
#
#
# naive_bayes_model = SklearnClassifier(MultinomialNB())
#
# # train the model on the training data
# naive_bayes_model.train(train_data)
#
# # and test on the testing dataset!
# accuracy = nltk.classify.accuracy(naive_bayes_model, test_data) * 100
# print("Naive Bayes Classifier Accuracy: {}".format(accuracy))
#
# # make class label prediction for testing set
# txt_features, labels = zip(*test_data)
#
# print(txt_features[:10])
# naive_bayes_prediction = naive_bayes_model.classify_many(txt_features)
#
# print(len(naive_bayes_prediction))
#
# # print a confusion matrix and a classification report
# print(classification_report(labels, naive_bayes_prediction))
#
# print(pd.DataFrame(
#     confusion_matrix(labels, naive_bayes_prediction),
#     index=[['actual', 'actual'], ['positive', 'negative']],
#     columns=[['predicted', 'predicted'], ['positive', 'negative']]))
