from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "fraud-results-topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Waiting for results...\n")

for msg in consumer:
    print("RESULT:", msg.value)