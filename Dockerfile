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

VOLUME /home/yd/PycharmProjects/Company-CRM-Example

EXPOSE 8000

# runs the production server
#ENTRYPOINT ["python", "mysite/manage.py"]
#ENTRYPOINT ["python", "manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]
#CMD bash -c "python manage.py runserver 0.0.0.0:8000 &&  \
#    celery -A crm_for_companies worker -l info -E && \
#    celery -A crm_for_companies beat -l info"
COPY entrypoint.sh entrypoint.sh

# Following command also should be executed on host machine
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]
#RUN /code/entrypoint.sh