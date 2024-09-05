# PythonRabbitMq
> Minimal code to Test RabbitMQ queue messages

## Execute RabbitMQ
```bash
$ docker-compose up -d
```

## Check if RabbitMQ is working
 - http://localhost:5672

## RabbitMQ Credentials
 - user: guest
 - password: guest

## RabbitMQ queue name
 - test

## Execute consumer
```bash
$ cd src/consumer/
$ docker-compose up --build
```

## Execute publisher
```bash
$ cd src/publisher/
$ docker-compose up --build
```

## Future work
 - Consumer need to be modified to never close connection after consume message

## Acknowledgements
 - [RabbitMq Python](https://www.rabbitmq.com/tutorials/tutorial-three-python)
