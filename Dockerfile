# create me my Dockerfile
FROM python:3.8-slim

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# set the working directory to /app
WORKDIR /app

# copy the content of the local directory to the working directory
COPY . /app

# Expose port 5000
EXPOSE 5000

# run the command to start app
CMD flask run --host 0.0.0.0 --port=5000