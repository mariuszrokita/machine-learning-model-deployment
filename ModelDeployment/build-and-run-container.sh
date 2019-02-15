#!/bin/sh
 
#echo ***Building titanic-passengers-api:latest***
#docker build -t titanic-passengers-api:latest .
 
#echo ***Running the container***
#docker run -d -p 5000:80 titanic-passengers-api
 
echo ***Building image and running the container***
docker-compose up --build
 
echo ***View running app***
python -m webbrowser -t "http://localhost:5000"