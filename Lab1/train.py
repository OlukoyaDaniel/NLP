
# coding: utf-8

# In[1]:


import csv


# ### Reading various data from text files

# In[2]:


with open('vocabulary.txt') as v:
    vocabulary = v.readlines()
    vocabulary = [x.strip('\n') for x in vocabulary]


# In[3]:


with open('documents.txt') as d:
    documents = d.readlines()
    documents = [x.strip('\n') for x in documents]


# In[4]:


with open('positive_documents.txt') as pd:
    positive_documents = pd.readlines()
    positive_documents = [x.strip('\n') for x in positive_documents]


# In[5]:


with open('negative_documents.txt') as nd:
    negative_documents = nd.readlines()
    negative_documents = [x.strip('\n') for x in negative_documents]


# In[6]:


with open('positive_words.txt') as pw:
    positive_words = pw.readlines()
    positive_words = [x.strip('\n') for x in positive_words]


# In[7]:


with open('negative_words.txt') as nw:
    negative_words = nw.readlines()
    negative_words = [x.strip('\n') for x in negative_words]


# In[8]:


word_likelihood = dict()


# ### Writing all the data of the words , their positive & negative likelihoods along with their count to a dictionary

# In[9]:


for word in vocabulary:
    if word not in word_likelihood:
        negative_word_count = 0
        positive_word_count = 0
        for pword in positive_words:
            if word == pword:
                positive_word_count += 1
        positive_word_freq = (positive_word_count + 1) / (len(positive_words) + len(word_likelihood))
        for nword in negative_words:
            if word == nword:
                negative_word_count += 1
        negative_word_freq = (negative_word_count + 1) / (len(negative_words) + len(word_likelihood))
        word_likelihood[word] = {'positive': positive_word_freq, 'negative': negative_word_freq, 'count': 1}

    else:
        word_likelihood[word]['count'] += 1


# ### Writing the data stored in the word_likelihood dicitonary to the csv file

# In[10]:


with open('Word_Likelihood.csv', mode='w') as csv_file:
    fieldnames = ['word', 'positive', 'negative', 'word_count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for word in word_likelihood:
        writer.writerow({'word': word, 'positive': word_likelihood.get(word).get('positive'),
                         'negative': word_likelihood.get(word).get('negative'),
                         'word_count': word_likelihood.get(word).get('count')})

