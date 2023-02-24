FROM python:3.10-slim-buster

# current working directory inside container
WORKDIR /backend-flask

# copy requirements from host to container
COPY requirements.txt requirements.txt
# install Python libraries inside container
RUN pip3 install -r requirements.txt

# copy everything from host machine current dirrectory
# to container current directory
COPY . .

# set the env var inside the container
ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]