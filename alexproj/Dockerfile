FROM python:3.8
WORKDIR /alexproj/tests
COPY testInterests.py /tests/

RUN pip install nltk

COPY . .

CMD ["stdbuf", "-oL", "python3", "./tests/testInterests.py"]