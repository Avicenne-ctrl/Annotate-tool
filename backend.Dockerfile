FROM python:3.12-slim

WORKDIR /source
COPY . ./
RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["uvicorn", "--workers", "1", "--host", "0.0.0.0", "--port", "5000", "source.main:app"]
