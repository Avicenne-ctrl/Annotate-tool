FROM python:3.10.4 as build

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "source/app.py"]
