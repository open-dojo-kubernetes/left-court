import pika


class ScoreNotifier(object):

    def __init__(self):
        self.host = 'localhost'
        self.exchange = 'score-queue-exchange'
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))

    @staticmethod
    def get_score_payload(winner: str, count: int) -> str:
        return dict(pointWinner=winner, playsCount=count).__str__()

    def publish_winner(self, side: str, count: int):
        print('Account point for ', side)
        routing_key = 'scores-python'
        try:
            self.connection.channel().basic_publish(exchange=self.exchange,
                                                    routing_key=routing_key,
                                                    body=self.get_score_payload(winner=side, count=count))
        except ConnectionError:
            print("DAMN YOU WABBIT!")
        print("[x] Sent Score to Queue")

    def notify_my_point(self, count: int):
        self.publish_winner('LEFT', count)

    def notify_foe_point(self, count: int):
        self.publish_winner('RIGHT', count)






