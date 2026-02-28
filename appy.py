# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask uses
EXPOSE 8080

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
