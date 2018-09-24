
# coding: utf-8

# ### Importing and opening the necessary files needed

# In[10]:


import csv

results = open("result.txt", "w+")
results.truncate(0)

# ### Function that takes a sentence as a parameter and return the class in which it falls into

# In[4]:


def test(sentence):
    
    #opening the various text files and storing the data in lists
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

    #Getting the total number of documents
    number_of_documents = len(documents)
    
    #Getting the number of positive documents
    number_of_all_pdocs = len(positive_documents)
    
    #Getting the number of negative documents
    number_of_all_ndocs = len(negative_documents)

    #Calculating the log prior for the positive class
    positive_logprior = number_of_all_pdocs / number_of_documents
    
    #Calculating the log prior for the negative class
    negative_logprior = number_of_all_ndocs / number_of_documents

    #dictionary to store the data that would be retrieved from a csv
    trained_data = dict()

    #reading data in from a csv and wrting them into the trained_data dictionary
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
        


# ### Determining the class of text that would be passed in from a text file and ouputing it into a results file.

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
    


# In[ ]:


def run():
    text_file=input('Please enter the filename with the (.txt) extension: ')
    print('This might take about 2 minutes')
    main(str(text_file))
    print('Process completed check the results.txt file')

run()
