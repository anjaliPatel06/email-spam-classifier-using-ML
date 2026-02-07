# 📧 Email Spam Classification System

An end-to-end **Machine Learning** project that classifies email messages as **Spam** or **Ham (Not Spam)** using **Natural Language Processing (NLP)** techniques.  
The application is deployed using **FastAPI** for the backend, **Streamlit** for the frontend, and **Docker** for containerization.

---

## 🚀 Features
- Spam email detection using Naive Bayes
- Text preprocessing and feature extraction using TF-IDF
- FastAPI REST API for model inference
- Streamlit-based interactive user interface
- Dockerized application (single container)
- Swagger UI for API testing

---

## 🧠 Tech Stack
- Python
- Scikit-learn
- NLTK
- FastAPI
- Streamlit
- Docker

---

## ⚙️ How the Application Works
1. User enters an email message in the Streamlit UI  
2. Streamlit sends the message to the FastAPI `/predict` endpoint  
3. FastAPI preprocesses the text and applies the trained ML model  
4. The prediction result (Spam / Ham) is returned to the frontend  

---

## 🐳 Run the Project Using Docker

### Step 1: Build Docker Image
```bash
docker build -t email-spam-app .
