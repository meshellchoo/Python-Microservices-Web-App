import json
import pika

params = pika.URLParameters('amqps://wagvnhuu:7d-_cDEpJp91U-CXR3RGw_Cofndxbrt8@gull.rmq.cloudamqp.com/wagvnhuu')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

