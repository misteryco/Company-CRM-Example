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

EXPOSE 8000

COPY entrypoint.sh entrypoint.sh
#RUN chmod +x entrypoint.sh
# runs the production server
#ENTRYPOINT ["python", "mysite/manage.py"]
#ENTRYPOINT ["python", "manage.py"]
#CMD ["python3", "runserver", "0.0.0.0:8000"]
#CMD bash -c "python manage.py runserver 0.0.0.0:8000 &&  \
#    celery -A crm_for_companies worker -l info -E && \
#    celery -A crm_for_companies beat -l info"
#COPY entrypoint.sh entrypoint.sh
#RUN chmod +x entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]
#RUN /code/entrypoint.sh
