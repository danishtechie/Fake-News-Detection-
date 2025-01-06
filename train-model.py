import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# Load preprocessed data
train_path = os.path.join('..', 'processed_data', 'train.csv')
test_path = os.path.join('..', 'processed_data', 'test.csv')

# Load data
train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

# Separate features and labels
X_train, y_train = train['text'], train['label']
X_test, y_test = test['text'], test['label']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_tfidf, y_train)


predictions = model.predict(X_test_tfidf)


print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))

# Save Model and Vectorizer
output_path = os.path.join('..', 'models')
os.makedirs(output_path, exist_ok=True)

joblib.dump(model, os.path.join(output_path, 'fake_news_model.pkl'))
joblib.dump(vectorizer, os.path.join(output_path, 'tfidf_vectorizer.pkl'))

print("Model and vectorizer saved successfully!")
