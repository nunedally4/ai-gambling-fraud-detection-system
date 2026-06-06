from flask import Flask, render_template_string
from kafka import KafkaConsumer
import threading
import json

app = Flask(__name__)

result = "Waiting..."

HTML = """
<h2>Fraud Result Dashboard</h2>
<p>{{result}}</p>
"""

def listen():
    global result

    consumer = KafkaConsumer(
        "fraud-results-topic",
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    for msg in consumer:
        result = str(msg.value)

threading.Thread(target=listen, daemon=True).start()

@app.route("/")
def home():
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(port=5001, debug=True)