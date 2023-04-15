FROM python:3.11.0

# same as running python with "-u"
ENV PYTHONUNBUFFERED 1

RUN mkdir /ticketsite
COPY . /ticketsite/
WORKDIR /ticketsite

RUN pip install -r requirements.txt
