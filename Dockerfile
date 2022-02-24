# using python 3.7 as base image
FROM python:3.7-slim 

# installing the flask module
RUN pip install flask

# create the application environment
WORKDIR /app 

# copy the application to the working directory
COPY ./demo.py ./ 

# command to execute when the container starts
ENTRYPOINT [ "python","demo.py" ]

