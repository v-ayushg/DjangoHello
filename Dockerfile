# Use an official Python runtime as a parent image
FROM python:3.12

# set the working directory in the container
WORKDIR /code


# copy the dependecies file to the working directory
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
