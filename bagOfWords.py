import pandas as pd
from bs4 import BeautifulSoup
import re
#nltk.download()  # Download text data sets, including stop words
from nltk.corpus import stopwords  # Import the stop word list


def review_to_words(raw_review):
    review_text = BeautifulSoup(raw_review).get_text()
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    words = letters_only.lower().split()
    stop_words = set(stopwords.words("english"))
    meaningful_words = [w for w in words if w not in stop_words]
    return (" ".join(meaningful_words))

train = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)
num_reviews = train["review"].size
clean_train_reviews = []

for i in xrange(0, num_reviews):
    if((i + 1) % 1000 == 0):
        print "Review %d of %d\n" % (i + 1, num_reviews)
    clean_train_reviews.append(review_to_words(train["review"][i]))
