# # django 4.1

# FROM  python:3.8.13-bullseye
# 3.10.4

# ENV PYTHONUNBUFFERED=1

# WORKDIR /api

# RUN pip install django django-cors-headers

# # copy from the current directory of the Dockerfile to /api in the image
# COPY . . 

# EXPOSE 8000


# Base image
FROM python:3.10-alpine
# python:3.8.13-bullseye 
# python:3.10.4-alpine
# python:3.10.4-slim-buster 


# Set working directory
WORKDIR /backend-app

# Install system dependencies
RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=myapp.settings
ENV PYTHONUNBUFFERED=1

# Collect static files
RUN python manage.py collectstatic --no-input

# Expose port
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]