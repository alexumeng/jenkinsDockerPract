FROM python:3.8

WORKDIR /alexproj/

COPY requirements.txt requirements.txt
RUN pip install nltk

COPY . .

CMD ["python3", "Main.py", "./testInterests.py"]