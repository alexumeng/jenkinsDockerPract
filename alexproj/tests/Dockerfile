FROM python:3.8

WORKDIR /alexproj/tests/

COPY requirements.txt requirements.txt
RUN python -m unittest 

COPY . .

CMD ["python3", "./testInterests.py"]