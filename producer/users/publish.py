import os
import json

import pika

from users.parse_data import get_users


def publish(message):
    """
    """
    rabbitmq_host = os.environ.get('RABBITMQ_HOST')
    connection_mq = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host))
    channel = connection_mq.channel()

    channel.queue_declare(queue='users-info-queue')

    channel.basic_publish(exchange='users', routing_key='users.info',
                          body=json.dumps(message))
    connection_mq.close()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))
