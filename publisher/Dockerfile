# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 80

# Define the command to run the Flask application
CMD ["python", "publisher.py"]

# run command: docker build -t flask-mqtt-app .
# run command: docker run -d -p 5000:5000 -p 1883:1883 flask-mqtt-app

