from flask import Flask, render_template, request
from predict import predict_news, highlight_fake_content

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/', methods=['GET'])
def home():
    # Render template with no predictions initially
    return render_template('index.html', prediction=None, confidence=None, highlights=[], error=None)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch input from form
        news = request.form.get('news', '').strip()

        # Handle empty input
        if not news:
            return render_template('index.html',
                                   prediction=None,
                                   confidence=None,
                                   highlights=[],
                                   error="Please enter some news text!")

        # Get prediction and confidence
        result, confidence = predict_news(news)

        # Highlight suspicious words if it's 'Fake News'
        highlights = highlight_fake_content(news) if result == "Fake News" else []

        # Render results in template
        return render_template('index.html',
                               prediction=result,
                               confidence=confidence,
                               highlights=highlights,
                               error=None)

    except ValueError as e:
        # Handle ValueError and display error
        return render_template('index.html',
                               prediction=None,
                               confidence=None,
                               highlights=[],
                               error=f"ValueError: {str(e)}")

    except Exception as e:
        # Handle unexpected errors
        return render_template('index.html',
                               prediction=None,
                               confidence=None,
                               highlights=[],
                               error="An unexpected error occurred. Please try again.")

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
