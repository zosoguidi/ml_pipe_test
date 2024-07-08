# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3.9 -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

#USER root

# update repos
# RUN apt-get update && apt-get install -y python3 python3-pip g++ cron 
# RUN apt-get update && apt-get install -y python3.9 python3.9-dev g++ cron 

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential cron && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY /app /app

# map volume
VOLUME /app2


COPY crontab_isert /etc/cron.d/crontab_isert
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontab_isert

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
 
# Apply the cron job
RUN crontab /etc/cron.d/crontab_isert

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log

