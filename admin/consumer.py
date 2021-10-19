# amqps://vqvsnzwi:p4o0gQsPcvf4JnNnqB04j2Gx__C03UCq@rattlesnake.rmq.cloudamqp.com/vqvsnzwi

import pika
# helps to send events

params = pika.URLParameters('amqps://vqvsnzwi:p4o0gQsPcvf4JnNnqB04j2Gx__C03UCq@rattlesnake.rmq.cloudamqp.com/vqvsnzwi')

connecton = pika.BlockingConnection(params)

channel = connecton.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('started consuming')

channel.start_consuming()
channel.close()