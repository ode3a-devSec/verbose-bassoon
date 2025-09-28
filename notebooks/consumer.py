from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id='test-group'
)

for msg in consumer:
    print(f"Received: {msg.value.decode('utf-8')}")