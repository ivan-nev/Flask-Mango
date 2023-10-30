# pull official base image
FROM python:3.11.2-alpine

# Set the working directory in the container
WORKDIR /app

# Скачиваем/обновляем необходимые библиотеки для проекта
COPY requirements_prod.txt /app



RUN apk update \
    && apk add git

# Install any dependencies
RUN pip3 install --upgrade pip -r requirements_prod.txt

# Copy the content of the project directory to the working directory
COPY . /app

#
## By default, listen on port 5000
EXPOSE 5000

