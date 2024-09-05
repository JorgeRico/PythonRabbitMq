import pika

class RabbitMQ:
    def __init__(self):
        self.user       = "guest"
        self.password   = "guest"
        self.host       = "rabbitmq"
        self.port       = int(5672)
        self.connection = None
        self.channel    = None
        self.response   = None
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

    # consume message queued on rabbitmq
    def consume(self, queue_name):
        print(' [*] Waiting for messages. To exit press CTRL+C')

        if not self.channel:
            raise Exception(" !!! Connection is not established.")
        
        def callback(ch, method, properties, body):
            print(f" [x] Received: {body.decode()}")
            print(" [x] Done")
            ch.stop_consuming()

        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        self.channel.start_consuming()
 