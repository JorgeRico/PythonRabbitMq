from rabbitmq import RabbitMQ
import sys

def main():
    rabbitmq = RabbitMQ()
    queue    = "test"

    try:
        print(" [*] Connection to RabbitMQ established successfully.")
        rabbitmq.consume(queue_name=queue)

    except Exception as e:
        print(f" !!! Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)
    finally:
        rabbitmq.close()

    
# execute code
main()