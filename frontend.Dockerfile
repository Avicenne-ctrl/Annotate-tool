FROM python:3.12-slim

ENV ENVIRONMENT="dev"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y libicu-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . ./

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "source/app.py"]
