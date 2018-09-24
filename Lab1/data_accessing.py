
# coding: utf-8

# ### Creating text documents to store the various classes of the data respectively

# In[ ]:


positive_words = open("positive_words.txt", "w+")
negative_words = open("negative_words.txt", "w+")
positive_documents = open("positive_documents.txt", "w+")
negative_documents = open("negative_documents.txt", "w+")
vocabulary = open("vocabulary.txt", "w+")
documents = open("documents.txt", "w+")


# ### Creating lists to store the data respectively gotten from the text documents

# In[2]:


lpositive_words = []
lnegative_words = []
lpositive_documents = []
lnegative_documents = []
lvocabulary = []
ldocuments = []


# ### Importing all the text documents to access the data and tokenizing the words

# In[3]:


with open('yelp_labelled.txt') as y:
    yelp_content = y.readlines()
    yelp_content = [x.replace("-", '\n').replace(":", '\n').replace(";", '\n').replace("*", '\n').replace("%", '\n').replace("&", '\n').replace("/", '\n').strip('\n').replace('.', '').replace('!', '').replace('"', '').replace(")", '').replace("(",
                                                                                                          '').replace(
        "?", '').replace(",", '') for x in yelp_content]


# In[4]:


for docs in yelp_content:
    clss = docs.split('\t')
    documents.write(clss[0].lower() + '\n')
    ldocuments.append(clss[0].lower())
    if clss[1] == '1':
        positive_documents.write(clss[0].lower() + '\n')
        lpositive_documents.append(clss[0].lower())
    elif clss[1] == '0':
        negative_documents.write(clss[0].lower() + '\n')
        lnegative_documents.append(clss[0].lower())


# In[5]:


with open('imdb_labelled.txt') as i:
    imdb_content = i.readlines()
    imdb_content = [x.replace("-", '\n').replace(";", '\n').replace(":", '\n').replace("/", '\n').replace("%", '\n').replace("&", '\n').replace("*", '\n').strip('\n').replace('.', '').replace('!', '').replace('"', '').replace(")", '').replace("(",
                                                                                                          '').replace(
        "?", '').replace(",", '') for x in imdb_content]


# In[6]:


for docs in imdb_content:
    clss = docs.split('\t')
    documents.write(clss[0].lower() + '\n')
    ldocuments.append(clss[0].lower())
    if clss[1] == '1':
        positive_documents.write(clss[0].lower() + '\n')
        lpositive_documents.append(clss[0].lower())
    elif clss[1] == '0':
        negative_documents.write(clss[0].lower() + '\n')
        lnegative_documents.append(clss[0].lower())


# In[7]:


with open('amazon_cells_labelled.txt') as a:
    amazon_content = a.readlines()
    amazon_content = [x.replace("-", '\n').replace(";", '\n').replace(":", '\n').replace("/", '\n').replace("%", '\n').replace("&", '\n').replace("*", '\n').strip('\n').replace('.', '').replace('!', '').replace('"', '').replace(")", '').replace("(",
                                                                                                          '').replace(
        "?", '').replace(",", '') for x in amazon_content]


# In[8]:


for docs in amazon_content:
    clss = docs.split('\t')
    documents.write(clss[0].lower() + '\n')
    ldocuments.append(clss[0].lower())
    if clss[1] == '1':
        positive_documents.write(clss[0].lower() + '\n')
        lpositive_documents.append(clss[0].lower())
    elif clss[1] == '0':
        negative_documents.write(clss[0].lower() + '\n')
        lnegative_documents.append(clss[0].lower())


# In[9]:


for doc in ldocuments:
    words = doc.split()
    for word in words:
        vocabulary.write(word.lower() + '\n')


# In[10]:


for doc in lpositive_documents:
    words = doc.split()
    for word in words:
        positive_words.write(word.lower() + '\n')


# In[11]:


for doc in lnegative_documents:
    words = doc.split()
    for word in words:
        negative_words.write(word.lower() + '\n')

