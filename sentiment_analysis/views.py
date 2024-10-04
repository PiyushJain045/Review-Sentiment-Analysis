from django.shortcuts import render
import joblib
import os
from django.conf import settings

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        review = request.POST.get('review')

        model_path = os.path.join(settings.BASE_DIR, 'sentiment_analysis/ml_model/sentiment_model.pkl')
        vectorizer_path = os.path.join(settings.BASE_DIR, 'sentiment_analysis/ml_model/vectorizer.pkl')

        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)

        # When new data is received from the frontend
        user_input = review
        input_vectorized = vectorizer.transform([user_input])  # Transform using the saved vectorizer
        print("vector:", input_vectorized)

        # Make a prediction
        prediction = model.predict(input_vectorized)
        print(prediction[0])
 
        return render(request, "sentiment_analysis/predict.html", {"prediction": prediction[0]})
    
    return render(request, "sentiment_analysis/home.html")
