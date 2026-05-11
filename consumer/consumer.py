import json
from kafka import KafkaConsumer
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://172.27.116.86:27017/")

db = client["iot_db"]

collection = db["sensor_data"]

# Connect to Kafka
consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers='localhost:9094',

    auto_offset_reset='earliest',

    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started...")

# Read messages from Kafka
for message in consumer:

    data = message.value

    print("Received:", data)

    collection.insert_one(data)

    print("Inserted into MongoDB")
