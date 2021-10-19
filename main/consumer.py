# amqps://vqvsnzwi:p4o0gQsPcvf4JnNnqB04j2Gx__C03UCq@rattlesnake.rmq.cloudamqp.com/vqvsnzwi

from main import Product, db
import pika, json
# helps to send events

params = pika.URLParameters('amqps://vqvsnzwi:p4o0gQsPcvf4JnNnqB04j2Gx__C03UCq@rattlesnake.rmq.cloudamqp.com/vqvsnzwi')

connecton = pika.BlockingConnection(params)

channel = connecton.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)
    # Creating objects with sql alchemy
    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title =data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')
    else:
        print('No function was executed')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack = True)

print('started consuming')

channel.start_consuming()
channel.close()