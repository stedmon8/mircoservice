import pika, json

params = pika.URLParameters('amqps://tfvbaylc:JbZiLMPItOgKhLII2ITNnTWuxDdKXmIR@shrimp.rmq.cloudamqp.com/tfvbaylc')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)