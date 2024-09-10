# syntax=docker/dockerfile:1

# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory within the Docker container to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt requirements.txt

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the working directory
COPY . .

# Copy the .env file into the container
COPY .env .env

# Expose port 5000 to the host machine
EXPOSE 5000

# Set environment variable for Flask app entry point
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
