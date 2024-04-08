#Set up a base image for your container
FROM python:3.11.9

#Create a working directory for the container for the application
WORKDIR /app


#Copy the contens of the requirements.txt file into a tmp folder
COPY requirements.txt /tmp/requirements.txt

#install packags in the requirements.txt file
RUN python -m pip install --timeout 300000 -r requirements.txt


#copy all the files and folders into the contaier's working directory
COPY . /app

EXPOSE 8077

#Run the fastAPI application
CMD ['uvicorn', 'main:app', '--host'. '0.0.0.0', '--port', 8077]

