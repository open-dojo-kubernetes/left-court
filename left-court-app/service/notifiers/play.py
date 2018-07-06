import pika

class PlayNotifier(object):
    def __init__(self,):
        self.host = 'localhost'
        self.connection = pika.AsyncioConnection(pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()

    def publish_play(self, play: dict, gameIdentifier: int):
        exchange = 'plays-exchange'.format(gameIdentifier)
        routing_key = 'left-side-plays'.format(gameIdentifier)
        try:
            self.channel.basic_publish(exchange=exchange,
                                                    routing_key=routing_key,
                                                    body=play)
        except ConnectionError:
            print("DAMN YOU WABBIT!")
        print("[x] Sent Score to Queue")

    def receive_play(self):
        while self.channel.is_open:
            try:
                self.channel.basic_consume(queue='right-side-plays',consumer_callback=on_receive_play_callback)
            except pika.exceptions.ConnectionClosedByBroker:
                print('Connection closed by broker')
                break
            except pika.exceptions.AMQPChannelError:
                print('Channel error on AMQP')
                break
            except pika.exceptions.AMQPConnectionError:
                print('Connection error, retrying...')
                continue



