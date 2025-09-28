from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='kafka:9092')


for i  in range(10):
    message = f'Hello kafka {i}'.encode('utf-8')
    producer.send('test-topic', value=message)
    print(f'Sent: {message}')

producer.flush()
producer.close()