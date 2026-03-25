from flask import Flask, request, render_template
import pickle
from preprocess import clean_text

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    confidence = None
    if request.method == 'POST':
        email_text = request.form['email_text']
        cleaned = clean_text(email_text)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        proba = model.predict_proba(vectorized)[0]
        result = 'PHISHING' if prediction == 1 else 'SAFE'
        confidence = round(max(proba) * 100, 2)
    return render_template('index.html', result=result, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
