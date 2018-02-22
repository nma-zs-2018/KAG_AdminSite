FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# Add crontab file in the cron directory
ADD crontab /cron.d/cron

# Give execution rights on the cron job
RUN chmod 0644 /cron.d/cron

# Run the command on container startup
CMD cron

CMD python3 manage.py runserver 0.0.0.0:8000