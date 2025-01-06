import joblib
from lime.lime_text import LimeTextExplainer
import numpy as np

# Load model and vectorizer
model = joblib.load('models/fake_news_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')


# Prediction function with confidence
def predict_news(news_text):
    # Transform the input into vectorized format
    data = vectorizer.transform([news_text])  # Ensure 2D input

    # Make the prediction
    prediction = model.predict(data)[0]

    # Get confidence score
    confidence_scores = model.predict_proba(data)[0]
    confidence = round(confidence_scores[1] * 100, 2) if prediction == 1 else round(confidence_scores[0] * 100, 2)

    # Return prediction and confidence score
    return ("Fake News" if prediction == 0 else "Real News", confidence)


# Create a wrapper for LIME to handle raw text input
def lime_wrapper(texts):
    # Convert raw text into vectorized format
    data = vectorizer.transform(texts)
    return model.predict_proba(data)


# Highlight suspicious words for fake content
def highlight_fake_content(news):
    # LIME Text Explainer
    explainer = LimeTextExplainer(class_names=["Fake", "Real"])

    # Generate explanation using the custom wrapper
    exp = explainer.explain_instance(news, lime_wrapper, num_features=10)

    # Extract highlighted suspicious words
    highlighted_words = [word for word, weight in exp.as_list() if weight < 0]
    return highlighted_words
