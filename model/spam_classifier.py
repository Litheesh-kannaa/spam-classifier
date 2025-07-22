import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, '..', 'spam.csv')

df = pd.read_csv(csv_path, encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X_train, _, y_train, _ = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vectors, y_train)

with open(os.path.join(BASE_DIR, 'model.pkl'), 'wb') as f:
    pickle.dump(model, f)

with open(os.path.join(BASE_DIR, 'vectorizer.pkl'), 'wb') as f:
    pickle.dump(vectorizer, f)

def classify_email(email_text):
    with open(os.path.join(BASE_DIR, 'model.pkl'), 'rb') as f:
        model = pickle.load(f)
    with open(os.path.join(BASE_DIR, 'vectorizer.pkl'), 'rb') as f:
        vectorizer = pickle.load(f)

    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    return "Spam" if prediction == 1 else "Not Spam"