FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    cron \
    wget \
    gnupg \
    dos2unix

#set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

RUN echo "*/30 * * * * /bin/bash /app/run.sh >> /app/logs/main.log 2>&1" > /etc/cron.d/my_cron
RUN chmod 755 /etc/cron.d/my_cron
RUN crontab /etc/cron.d/my_cron
RUN service cron start

WORKDIR /app

COPY . /app/
RUN mkdir /app/logs && touch /app/logs/main.log

RUN pip install -r requirements.txt

RUN chmod 755 /app/entrypoint.sh
RUN chmod 755 /app/run.sh

RUN dos2unix /app/entrypoint.sh && dos2unix /app/run.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["cron", "-f"]
