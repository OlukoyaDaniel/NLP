
# coding: utf-8

# In[10]:


import csv

results = open("result.txt", "w+")


# In[4]:


def test(sentence):
    with open('vocabulary.txt') as v:
        vocabulary = v.readlines()
        vocabulary = [x.strip('\n') for x in vocabulary]

    with open('documents.txt') as d:
        documents = d.readlines()
        documents = [x.strip('\n') for x in documents]

    with open('positive_documents.txt') as pd:
        positive_documents = pd.readlines()
        positive_documents = [x.strip('\n') for x in positive_documents]

    with open('negative_documents.txt') as nd:
        negative_documents = nd.readlines()
        negative_documents = [x.strip('\n') for x in negative_documents]

    with open('positive_words.txt') as pw:
        positive_words = pw.readlines()
        positive_words = [x.strip('\n') for x in positive_words]

    with open('negative_words.txt') as nw:
        negative_words = nw.readlines()
        negative_words = [x.strip('\n') for x in negative_words]

    number_of_documents = len(documents)

    number_of_all_pdocs = len(positive_documents)
    number_of_all_ndocs = len(negative_documents)

    positive_logprior = number_of_all_pdocs / number_of_documents
    negative_logprior = number_of_all_ndocs / number_of_documents

    trained_data = dict()

    with open('Word_Likelihood.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            trained_data[row["word"]] = {'word': row['word'], 'positive': row["positive"], 'negative': row["negative"],
                                         'count': row["word_count"]}
            line_count += 1

    text = sentence.replace("-", '\n').replace(";", '\n').replace(":", '\n').replace("/", '\n').replace("%",
                                                                                                        '\n').replace(
        "&", '\n').replace("*", '\n').strip('\n').replace('.', '').replace('!', '').replace('"', '').replace(")",
                                                                                                             '').replace(
        "(",
        '').replace(
        "?", '').replace(",", '').replace("$", '').replace('"', '').replace('”', '').replace('“', '')

    text = text.split()

    pdoc_probability = 0
    ndoc_probability = 0

    # P(doc | class) * P(class)
    for t in text:
        if t.lower() in trained_data:
            d = trained_data[t.lower()]
            pdoc_probability += (float(d['positive']) * positive_logprior)
        else:
            prob = (1 / (len(positive_words) + len(trained_data))) * positive_logprior
            pdoc_probability += prob

    for t in text:
        if t.lower() in trained_data:
            d = trained_data[t.lower()]
            ndoc_probability += (float(d['negative']) * negative_logprior)

        else:
            prob = (1 / (len(negative_words) + len(trained_data))) * negative_logprior
            ndoc_probability += prob

    if pdoc_probability > ndoc_probability:
        return 1
    else:
        return 0
        


# In[5]:


def main(text_file):
    with open(text_file) as t:
        file = t.readlines()
        file = [
            x.replace("-", '\n').replace(":", '\n').replace(";", '\n').replace("*", '\n').replace("%", '\n').replace(
                "&", '\n').replace("/", '\n').strip('\n').replace('.', '').replace('!', '').replace('"', '').replace(
                ")", '').replace("(",
                                 '').replace(
                "?", '').replace(",", '') for x in file]

    for doc in file:
        result = test(str(doc))
        results.write(str(result) + '\n')

