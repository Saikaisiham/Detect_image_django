import pika
import multiprocessing
from base.models import Message  
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Starts consuming messages from RabbitMQ'

    def on_message_received(self, ch, method, properties, body):
        # Body contains the binary message content received from RabbitMQ
        # .decode('utf-8') is used to convert the binary content to a Unicode string
        message_body = body.decode('utf-8')

        message = Message(message=message_body)  
        message.save()
        self.stdout.write(self.style.SUCCESS(f'Received new message: {message_body}'))

    def start_consuming(self):
        connection_parameters = pika.ConnectionParameters('localhost')
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        
        channel.queue_declare(queue='letterbox')
        
        channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=self.on_message_received)
        
        self.stdout.write(self.style.SUCCESS('Starting Consuming'))
        
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            connection.close()

    def handle(self, *args, **options):
        multiprocessing.Process(target=self.start_consuming).start()
