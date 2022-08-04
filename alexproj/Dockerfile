FROM python:latest

# install os dependent for python requirements to be installed
RUN set -x \
    && apt-get update && \
    apt-get install -y \
    libfreetype6-dev \
    default-libmysqlclient-dev \
    clamav

# RUN mkdir /alexproj

WORKDIR /tmp

# ADD . /alexproj
#COPY ./tests/testInterests.py /tests/

RUN pip install nltk

# RUN python -m unittest discover ./tests/

COPY . .

CMD ["python3", "./tests/testInterests.py"]

# CMD ["python3", "./tests/hello.py"]