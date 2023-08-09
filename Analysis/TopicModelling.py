import os
import numpy as np
import pandas as pd
import seaborn as sns
import string
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

# load the data collected from open source platform
df7 = pd.read_csv('/Users/ttonny0326/GitHub_Project/Topic_Modelling/News/Bloom_Berg_News.csv')
df7 = df7.drop_duplicates()

# data pre processing
nltk.download('stopwords')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    return [word for word in text if word not in stop_words]

# Function for removing punctuation
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator)

# Lowercase, remove punctuation, and tokenize the text
df7['processed_content'] = df7['Content'].str.lower()
df7['processed_content'] = df7['processed_content'].apply(remove_punctuation)
df7['processed_content'] = df7['processed_content'].str.split()
df7['processed_content'] = df7['processed_content'].apply(remove_stopwords)

# Convert lists in 'processed_text' back to strings
df7['processed_content'] = df7['processed_content'].apply(' '.join)

# load embedding model
transformer_embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
model = BERTopic(verbose=True, embedding_model=transformer_embedding_model, nr_topics='auto', calculate_probabilities=True)
# nr_topics='auto'
# configuration : min_topic_size=50,

# model training 
content_topics, probabilities = model.fit_transform(df7.processed_content)
os.environ['OMP_DISPLAY_ENV'] = 'FALSE'

model.visualize_topics()
model.visualize_hierarchy(top_n_topics=30)

# model save as a pickle file
model.save("BloomBerg_model_test", serialization="pickle")