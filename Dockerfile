FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# download nltk stopwords
RUN python -m nltk.downloader stopwords

# copy all project files
COPY . .

EXPOSE 8000
EXPOSE 8501

# directly run script with bash (no chmod needed)
CMD ["bash", "start.sh"]
