import os
import time

from kafka import KafkaProducer, KafkaConsumer

import logging
import argparse
logging.basicConfig(level=logging.INFO)


def produce_message(broker, topic, message):
    print(broker)
    producer = KafkaProducer(bootstrap_servers=broker,
                             api_version=(2, 0, 2),
                             )
    while True:
        future = producer.send(topic, message.encode('utf-8'))

        #print(f"Сообщение '{message}' отправлено в топик {topic} на брокер {broker}")



def consume_messages(broker, topic):


    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=broker,
        group_id=None,
        auto_offset_reset='earliest',
        api_version = (2,0,2)
    )

    for message in consumer:
        print(f"Получено сообщение: {message.value}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kafka producer and consumer')
    parser.add_argument('action', choices=['produce', 'consume'])
    parser.add_argument('--message', default=None)
    parser.add_argument('--topic', required=True)
    parser.add_argument('--kafka', required=True)

    args = parser.parse_args()
    print(f"Test some  : {args}")
    if args.action == 'produce':
        if args.message:
            produce_message(args.kafka, args.topic, args.message)
        else:
            print("Message is required for producing.")
    elif args.action == 'consume':
        consume_messages(args.kafka, args.topic)
