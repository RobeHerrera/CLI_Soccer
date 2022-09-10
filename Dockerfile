
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# create root directory for our project in the container
RUN mkdir /cli_soccer

# Set the working directory to /cli_soccer
WORKDIR /cli_soccer

# Copy the current directory contents into the container at /cli_soccer
ADD ./soccer_app /cli_soccer

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run actual CLI application
ENTRYPOINT [ "python", "main.py" ]