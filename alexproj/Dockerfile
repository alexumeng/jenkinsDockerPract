FROM python:3.8
WORKDIR /alexproj/tests
COPY ./tests/testInterests.py /tests/

RUN pip install nltk

COPY . .

CMD ["sh", "-c", "python3", "./tests/testInterests.py"]