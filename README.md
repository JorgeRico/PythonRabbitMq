# PythonRabbitMq
> Minimal code to Test RabbitMQ queue messages

## Execute RabbitMQ
> docker-compose up -d

## Check is rabbit working
> http://localhost:5672

## credentials
> user: guest
> password: guest

## RabbitMQ queue name
> test

## Execute consumer
> cd src/consumer/
> docker-compose up --build

## Execute publisher
> cd src/publisher/
> docker-compose up --build

## Future work
> Consumer need to be modified to never close connection after consume message