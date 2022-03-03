import pika

HOST = 'localhost'
QUEUE = 'example'

def callback(channel, method, properties, body):
    """
    Callback function to channel
    """
    print("[+] Received: {0}".format(body))

connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=HOST
        )
    )

channel = connection.channel()
channel.queue_declare(queue=QUEUE)

channel.basic_consume(
        on_message_callback=callback,
        queue=QUEUE,
        auto_ack=False
    )

print("[*] Listening..")

channel.start_consuming()