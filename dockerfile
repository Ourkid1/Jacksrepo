# Stage 1: Build the application
FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates/ ./templates/
COPY static/ ./static/

COPY . .

# Stage 2: Copy the built application and `.env` file to the final image
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /app /app

COPY .env .

# Load environment variables from .env file
RUN source /app/.env

# Set environment variable for Flask app entry point
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
