from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import json
import joblib

model = joblib.load("../fraud_model.pkl")

spark = SparkSession.builder.appName("FraudDetection").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions-topic") \
    .load()

data = df.selectExpr("CAST(value AS STRING)")

def process(batch_df, batch_id):
    from kafka import KafkaProducer

    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    rows = batch_df.collect()

    for r in rows:
        record = json.loads(r["value"])

        features = [[
            record["bet_amount"],
            record["time_between_bets"],
            record["odds"]
        ]]

        pred = model.predict(features)[0]

        result = {
            "fraud": int(pred),
            "original": record
        }

        producer.send("fraud-results-topic", result)

query = data.writeStream.foreachBatch(process).start()
query.awaitTermination()