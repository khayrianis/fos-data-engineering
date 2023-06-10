FROM python:latest

COPY . /fos-data-engineer

WORKDIR /fos-data-engineer

RUN apt-get update && apt-get -y install cron vim
RUN apt-get install gcc

RUN pip install -r requirements.txt

COPY cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN /usr/bin/crontab /etc/cron.d/cronfile
RUN echo $PYTHONPATH
# run crond as main process of container
CMD ["cron","-l 15", "-f"]


# CMD python etl.py

