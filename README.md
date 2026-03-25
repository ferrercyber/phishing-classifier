# Phishing Email Classifier

A machine learning web application that detects phishing emails using Natural Language Processing (NLP) and Logistic Regression.

## Overview

This project trains a classifier on a real-world dataset of 38,000+ emails to distinguish between phishing and legitimate emails with 99% accuracy. The model is served through a Flask web application where users can paste any email and get an instant prediction with a confidence score.

## Tech Stack

- Python
- scikit-learn (Logistic Regression, TF-IDF)
- NLTK (text preprocessing)
- Flask (web application)
- Pandas (data manipulation)

## How It Works

1. Raw email text is cleaned by removing URLs, special characters, and stopwords
2. Text is converted into numerical features using TF-IDF vectorization
3. A Logistic Regression model predicts whether the email is phishing or safe
4. The result and confidence score are displayed in the web app

## Model Performance

- Accuracy: 99%
- Precision: 0.99
- Recall: 0.99
- F1-Score: 0.99
- Dataset: CEAS 2008 - 38,669 emails

## Setup Instructions

1. Clone the repository
   git clone https://github.com/ferrercyber/phishing-classifier.git
   cd phishing-classifier

2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install pandas scikit-learn nltk flask

4. Download the CEAS 2008 dataset and save it as emails.csv in the project folder

5. Train the model
   python train.py

6. Run the web app
   python app.py

7. Visit http://127.0.0.1:5000 in your browser

## Project Structure

phishing-classifier/
+-- templates/
¦   +-- index.html
+-- app.py
+-- train.py
+-- preprocess.py
+-- explore.py
+-- .gitignore
+-- README.md
