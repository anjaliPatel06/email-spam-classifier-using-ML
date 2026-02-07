import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Email Spam Classifier", page_icon="📧")

st.title("📧 Email Spam Classifier")
st.write("Enter an email message and check whether it is **Spam** or **Ham**.")

email_text = st.text_area("✉️ Enter email text here", height=150)

if st.button("🔍 Predict"):
    if email_text.strip() == "":
        st.warning("Please enter an email message.")
    else:
        payload = {
            "email": email_text
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]

                if prediction == "spam":
                    st.error("This email is **SPAM**")
                else:
                    st.success("This email is **NOT SPAM (HAM)**")
            else:
                st.error("API error. Please check FastAPI server.")

        except Exception as e:
            st.error("Could not connect to FastAPI server.")
