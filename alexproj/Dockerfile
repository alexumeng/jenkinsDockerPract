FROM python:3.8

COPY ./alexproj /tests/
WORKDIR /alexproj/tests

RUN pip install nltk
RUN dotnet restore
RUN dotnet test --logger trx

COPY . .

CMD ["python3", "./tests/testInterests.py"]