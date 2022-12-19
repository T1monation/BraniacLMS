FROM python:3.10-alpine


WORKDIR /usr/src/BraniacLMS

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/BraniacLMS/entrypoint.sh
RUN chmod +x /usr/src/BraniacLMS/entrypoint.sh

# copy project
COPY . .


ENTRYPOINT ["/usr/src/BraniacLMS/entrypoint.sh"]