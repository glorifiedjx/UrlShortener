FROM ubuntu:latest
MAINTAINER John Kim "glorifiedjx@gmail.com"
RUN apt-get update -y

RUN apt-get install -y python3 python3-pip python3-dev build-essential curl

#Add source files
COPY . /app
WORKDIR /app

#Install Python web server and dependencies
RUN pip3 install -r requirements.txt

# Expose import
EXPOSE 5000

#ENTRYPOINT ["python", "manage.py", "initdb"]
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver"]
#CMD ["python", "manage.py", "runserver"]
