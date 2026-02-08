from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')

app = FastAPI()

class EmailRequest(BaseModel):
    email:str

# load the trained model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, "backend/model/nb_model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "backend/model/tfidf.pkl"), "rb"))


ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()                                                                   # lowercase
    text = re.sub(r'\d+', '', text)                                                       # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))                      # remove punctuation
    text = text.strip()                                                                   # remove leading/trailing spaces
    
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    
    return " ".join(words)



@app.get('/')
def home():
    return {"message": "Welcome to the email spam classifier API"}

@app.post('/predict')
def predict(request:EmailRequest):
    email = request.email
    cleaned_email = clean_text(email)
    email_vector = vectorizer.transform([cleaned_email])
    prediction = model.predict(email_vector)[0]

    return {
        "message":email,
        "prediction" : "spam" if prediction == 1 else "ham"
    }
print(vectorizer.vocabulary_.get("free"))
print(vectorizer.vocabulary_.get("win"))
print(vectorizer.vocabulary_.get("ticket"))

