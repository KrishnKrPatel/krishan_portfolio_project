# Use a Python 3.9-based image
FROM python:3.9.21-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies (useful for compiling C extensions)
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip


# Copy the requirements.txt and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code

COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000
