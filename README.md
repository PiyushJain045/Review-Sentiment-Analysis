# Django Sentiment Analysis Project
This Django-based web application analyzes the sentiment of user reviews, classifying them as either positive or negative. The project uses a pre-trained Logistic Regression machine learning model to perform sentiment analysis.

## Features
- User Input: Accepts user reviews from the frontend.
- Sentiment Classification: Uses a Logistic Regression model to classify reviews as positive or negative.
- ML Integration: The model and vectorizer are pre-trained and saved using joblib, and they are loaded dynamically for predictions.

## Installation 
Open the folder in your preferred IDE and execute the following commands <br>
Note: **it is preferred to creta a virtual environment first** <br>
- 1) pip install -r requirements.txt (Install dependencies) <br>
- 2) python manage.py migrate (setup sqlite3 db) <br>
- 3) python manage.py runserver (Run the Django development server) <br>

That's it! Access the web app at the URL provided by the Django development server (usually http://127.0.0.1:8000).
