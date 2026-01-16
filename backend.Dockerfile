FROM python:3.10.4 as build

WORKDIR /source
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "--workers"