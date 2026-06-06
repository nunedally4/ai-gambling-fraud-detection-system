from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    bet_amount = float(input("bet_amount: "))
    time_between_bets = float(input("time_between_bets: "))
    odds = float(input("odds: "))

    data = {
        "bet_amount": bet_amount,
        "time_between_bets": time_between_bets,
        "odds": odds
    }

    producer.send("transactions-topic", data)
    print("Sent:", data)