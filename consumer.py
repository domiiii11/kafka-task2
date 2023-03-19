from confluent_kafka import Consumer

################

consumer = Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})

print('Available topics to consume: ', consumer.list_topics().topics)

consumer.subscribe(['application_records'])

################

def main():
    while True:
        msg=consumer.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
        topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    consumer.close()
        
if __name__ == '__main__':
    main()