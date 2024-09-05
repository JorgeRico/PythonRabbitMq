import pika

class RabbitMQ:
    def __init__(self):
        self.user       = "guest"
        self.password   = "guest"
        self.host       = "rabbitmq"
        self.port       = int(5672)
        self.connection = None
        self.channel    = None
        self.connect()

    # connect with rabbitmq
    def connect(self):
        credentials     = pika.PlainCredentials(self.user, self.password)
        parameters      = pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel    = self.connection.channel()

    # close connection with rabbitmq
    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()

    # publish  message queued on rabbitmq
    def publish(self, queue_name, message):
        if not self.channel:
            raise Exception(" !!! Connection is not established.")
        
        self.channel.queue_declare(queue=queue_name)

        self.channel.basic_publish(
            exchange    = "",
            routing_key = queue_name,
            body        = message,
            # make message persistent
            properties  = pika.BasicProperties(delivery_mode = 2),
        )

        print (f" [x] Message sent to queue {queue_name}: {message}")