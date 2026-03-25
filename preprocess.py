import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()                          # Lowercase
    text = re.sub(r'http\S+|www\S+', '', text)        # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)           # Remove special chars
    tokens = text.split()
    tokens = [stemmer.stem(t) for t in tokens         # Stem words
              if t not in stop_words]                 # Remove stopwords
    return " ".join(tokens)