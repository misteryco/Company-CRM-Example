# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10
ENV PYTHONUNBUFFERED=1

# Allows docker to cache installed dependencies between builds

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

# Try to drop it
VOLUME /home/yd/PycharmProjects/Company-CRM-Example
# Try to drop it
EXPOSE 8000

COPY entrypoint.sh entrypoint.sh

# Following command also should be executed on host machine
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]
#RUN /code/entrypoint.sh