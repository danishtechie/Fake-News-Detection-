# Fake-News-Detection-


Fake News Detection Project
Developed by Danish Maqbool

Project Overview
This project is a Fake News Detection System designed to classify whether a given piece of news is real or fake based on the provided text. It uses Machine Learning algorithms to analyze the text and provides:

Prediction Result (Real or Fake)
Confidence Score (Percentage of accuracy for the prediction)
Highlighted Suspicious Words (To indicate parts that may suggest fake news)
Speech-to-Text Support (Allows input through voice commands)

Features:
Text Input Field: Users can paste or type news text directly.
Speech Recognition: Allows users to input text via voice commands.
Prediction Output: Displays the prediction (Fake or Real) with confidence percentage.
Highlighting Suspicious Words: Marks suspicious words for easier review.
Responsive UI: User-friendly design optimized for both desktop and mobile use.

Requirements:
Python 3.8 or higher
Flask Framework
Machine Learning Libraries:
scikit-learn
pandas
numpy
Natural Language Processing Tools:
nltk


Installation Guide
Clone the Repository:




Create a Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # For Linux/Mac
.\env\Scripts\activate   # For Windows

Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
Access the App in Your Browser:
Open http://127.0.0.1:5000/

Usage Instructions:
Input the News Text: Type or paste the news content into the provided text box.
Use Speech Input (Optional): Click the 🎤 button to activate voice input.
Check the Result: Press the Check button to analyze the input.
View Outputs: Check the prediction result, confidence score, and highlighted suspicious words.

Important Notes
Fair Usage: This tool is for educational and research purposes only. Do not use it for misinformation or malicious activities.
Data Privacy: No user data is stored or tracked. However, users should avoid submitting sensitive or personal information.
Limitations:
The prediction depends on training data and might not be 100% accurate.
Always double-check predictions with credible sources.

Developer Information
Name: Danish Maqbool
Contact: danishannu1111@gmail.com

License
This project is licensed under the MIT License. Feel free to modify or enhance the code but mention the original author when sharing or publishing it.
