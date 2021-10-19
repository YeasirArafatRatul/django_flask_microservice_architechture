# amqps://vqvsnzwi:p4o0gQsPcvf4JnNnqB04j2Gx__C03UCq@rattlesnake.rmq.cloudamqp.com/vqvsnzwi

import pika, json
# helps to send events

params = pika.URLParameters('amqps://vqvsnzwi:p4o0gQsPcvf4JnNnqB04j2Gx__C03UCq@rattlesnake.rmq.cloudamqp.com/vqvsnzwi')

connecton = pika.BlockingConnection(params)

channel = connecton.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
