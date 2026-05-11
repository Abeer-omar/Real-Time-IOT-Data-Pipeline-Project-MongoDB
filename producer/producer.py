import json
import time
import requests
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9094',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

URL = "https://api.thingspeak.com/channels/221538/feeds.json?results=1"

while True:

    response = requests.get(URL)

    data = response.json()

    latest_feed = data['feeds'][0]

    sensor_data = {
        "created_at": latest_feed.get("created_at"),
        "temperature": latest_feed.get("field1"),
        "humidity": latest_feed.get("field2"),
        "pressure": latest_feed.get("field3")
    }

    print("Sending:", sensor_data)

    producer.send(
        'sensor_data',
        value=sensor_data
    )

    producer.flush()

    time.sleep(5)
