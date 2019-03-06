FROM python:3.6-slim
RUN apt-get update -y
 
# Copy the current directory contents into the container at /app
COPY . /app
 
# Set the working directory to /app
WORKDIR /app
 
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
 
# Run app.py when the container launches
CMD ["python", "app.py"]
 
# Make port 80 available to the world outside this container
EXPOSE 80