# syntax=docker/dockerfile:1
# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

FROM python:3.9.13-slim-buster
# Set the working directory within the Docker container to /app
WORKDIR /app

COPY requirements.txt requirements.txt
# Copy the requirements.txt file from your local machine to the container
COPY requirements.txt .

RUN pip3 install -r requirements.txt
# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the templates and static folders
COPY templates/ ./templates/
COPY static/ ./static/

# Copy the rest of the application files
COPY . .
# Copy the .env file into the container
COPY .env .env

# Expose port 5000 to the host machine
EXPOSE 5000

# Set environment variable for Flask app entry point
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
