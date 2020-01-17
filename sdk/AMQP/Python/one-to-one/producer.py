# File: producer.py
# Description: This is the AMQP producer publishes outgoing AMQP
#     communication to  clients consuming messages from a broker server.
#     Messages can be sent over AMQP exchange types including one-to-one,
#     from broadcast pattern, or selectively using specified routing key.
#
# Author: Stanley
# robomq.io (http://www.robomq.io)

import pika

server = "hostname"
port = 5672
vhost = "yourvhost"
username = "username"
password = "password"
routingKey = "testQ"

try:
	#connect
	credentials = pika.PlainCredentials(username, password)
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = server, port = port, virtual_host = vhost, credentials = credentials, heartbeat_interval = 60))
	channel = connection.channel()

	#send message
	#assigning blank string to exchange is to use the default exchange, where queue name is the routing key
	properties = pika.spec.BasicProperties(content_type = "text/plain", delivery_mode = 1)
	channel.basic_publish(exchange = "", routing_key = routingKey, body = "Hello World!", properties = properties)

	#disconnect
	connection.close()
except Exception, e:
	print e