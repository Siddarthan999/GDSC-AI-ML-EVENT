FROM python:3-alpine3.15

# Install necessary system packages
RUN apk update && apk add --no-cache build-base python3-dev py3-pip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3000
EXPOSE 3000

# Command to run the application
CMD ["python", "./index.py"]
