FROM python:3.8

WORKDIR /testInterests

COPY requirements.txt requirements.txt
RUN python -m unittest testInterests.py

COPY . .

CMD ["python3", "testInterests.py"]