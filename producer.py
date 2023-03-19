from confluent_kafka import Producer
import json
import time
import logging
import csv
from read_cvs import get_application_records


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

producer = Producer({'bootstrap.servers':'localhost:9092'})

#####################

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)
        
#####################
print('Kafka Producer has been initiated...')

def main():   
    ids, applications_records_data = get_application_records()
    for i in range(len(ids)):
        id = ids[i]
        row_data= applications_records_data[i]
        applications_records_data_json = json.dumps(row_data)
        producer.poll(1)
        producer.produce(topic='application_records', key=id, value=applications_records_data_json.encode('utf-8'), callback=receipt)
        producer.flush()
        time.sleep(3)
        
if __name__ == '__main__':
    main()
