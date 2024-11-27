from kafka import KafkaProducer

# Configuration du producteur Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092')

def send_message_to_kafka(topic: str, message: str):
    producer.send(topic, value=message.encode('utf-8'))
    producer.flush()

