FROM python:3.10.4-alpine

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint
COPY ./entrypoint.sh ./entrypoint.sh
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# copy project
COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]