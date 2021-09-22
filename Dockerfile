# From tensorflow base image
FROM tensorflow/tensorflow:2.6.0

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD python /app/project/app.py 
