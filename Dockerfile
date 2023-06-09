FROM python:latest

COPY . /fos-data-engineer

WORKDIR /fos-data-engineer

RUN apt-get update && apt-get -y install cron
RUN apt-get install gcc

RUN pip install -r requirements.txt

# Run the Python script with cron
COPY cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile
CMD cron -f
