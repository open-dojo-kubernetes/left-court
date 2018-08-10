from retry import retry
import pika
import threading
import atexit
from flask import Flask

class PlayListener(object):
    def __init__(self):
        self.channel = pika.BlockingConnection(pika.ConnectionParameters('localhost')).channel()

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def consume(self):
        self.channel.basic_consume('right-side-plays', self.on_message_callback)
        try:
            self.channel.start_consuming()
        # Do not recover connections closed by server
        except pika.exceptions.ConnectionClosedByBroker:
            print('Connection error, retrying if AMQPConnectionError')
            pass

    def on_message_callback(self):
        print('Lets see what comes', self)