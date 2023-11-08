# producer.py
import pika

def send_message(message):
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    
    channel.queue_declare(queue='letterbox')
    
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    
    print(f'sent message: {message}')
    
    connection.close()
