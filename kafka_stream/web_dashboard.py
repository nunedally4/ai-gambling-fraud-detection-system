from flask import Flask, render_template_string
from kafka import KafkaConsumer
import threading
import json

app = Flask(__name__)

latest = "Waiting..."

HTML = """
<h2>Live Fraud Monitor</h2>
<p>{{data}}</p>
"""

def listen():
    global latest

    consumer = KafkaConsumer(
        "fraud-results-topic",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )

    for msg in consumer:
        latest = str(msg.value)

threading.Thread(target=listen, daemon=True).start()

@app.route("/")
def home():
    return render_template_string(HTML, data=latest)

if __name__ == "__main__":
    app.run(port=5001)