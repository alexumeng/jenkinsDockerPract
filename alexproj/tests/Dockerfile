FROM python:3.8

WORKDIR /alexproj/

COPY requirements.txt requirements.txt
RUN python -m unittest 

COPY . .

CMD ["python3", "/alexproj/Main.py", "./testInterests.py"]