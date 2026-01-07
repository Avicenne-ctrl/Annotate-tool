FROM python:3.11-slim
WORKDIR /source
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "source.main:app"]
