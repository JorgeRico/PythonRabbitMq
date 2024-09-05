from rabbitmq import RabbitMQ
import sys

def main():
    rabbitmq = RabbitMQ()
    queue    = "test"
    message  = "User information Message"

    try:
        print(" [*] Connection to RabbitMQ established successfully.")
        rabbitmq.publish(queue_name=queue, message=message)
    except Exception as e:
        print(f" !!! Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)
    finally:
        rabbitmq.close()


# execute code
main()