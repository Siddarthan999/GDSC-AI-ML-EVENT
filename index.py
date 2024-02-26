from flask import Flask
import re
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    phishing_urls = [
    "https://phishing-site1.com/login",
    "http://phishing-site2.ngrok.io",
    "https://phishing-site3.com/credentials",
    "https://379f-106-208-41-125.ngrok.io",
    "https://gmc-genetic-manage-currency.trycloudflare.com",
    "https://j5ibasixxx.loclx.io",
    "https://5006cc23690fb2.lhr.life"
    ]
    legitimate_urls = [
        "https://example.com/login",
        "http://example2.com/",
        "https://example3.com/home",
    ]
    all_urls = phishing_urls + legitimate_urls

    labels = [1] * len(phishing_urls) + [0] * len(legitimate_urls)

    vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
    X = vectorizer.fit_transform(all_urls)

    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Train a logistic regression classifier
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    # Predict on the test set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    def is_phishing_url(url):
        try:
            response = requests.get(url)
            html_content = response.text
        except:
            return True
        features = vectorizer.transform([html_content])
        prediction = clf.predict(features)
        return prediction[0] == 1

    urls = [ "https://get-blue-badge-on-twitter-free@5006cc23690fb2.lhr.life","https://www.google.com/" ]

    results = []

    for url in urls:
        if is_phishing_url(url):
            result = f"Model evaluation: \n Accuracy: {accuracy:.2f} \n Precision: {precision:.2f} \n Recall: {recall:.2f} F1-score: {f1:.2f} \n {url} is a potential phishing link."
        else:
            result = f"Model evaluation: \n Accuracy: {accuracy:.2f} \n Precision: {precision:.2f} \n Recall: {recall:.2f} F1-score: {f1:.2f} \n {url} is a legitimate link."
        results.append(result)

    return "<br>".join(results)

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("3000"), debug=True)