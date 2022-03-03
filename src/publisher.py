import pika

HOST = 'localhost'
QUEUE = 'example'

connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=HOST
        )
    )

channel = connection.channel()
channel.queue_declare(queue=QUEUE)

body = "testing channels"
routing_key = "example"

channel.basic_publish(
        exchange='',
        routing_key=routing_key,
        body=body
    )

connection.close()
