# AI Gambling Fraud Detection System

## Overview

AI Gambling Fraud Detection System is a real-time fraud detection platform that combines Machine Learning, FastAPI, Apache Kafka, and Apache Spark to identify suspicious betting activity.

The system receives betting data through an API, streams events using Kafka, processes them with Spark Streaming, and evaluates fraud risk using a trained machine learning model.

---

## Project Goal

The objective of this project is to automatically detect potentially fraudulent betting behavior by analyzing betting patterns in real time.

The system demonstrates how modern distributed technologies can be integrated with machine learning to build scalable fraud detection solutions.

---

## Problem Statement

Online gambling and sportsbook platforms process a large number of betting transactions every day. Detecting suspicious behavior manually is inefficient and time-consuming.

Examples of potentially fraudulent activity include:

* Extremely high betting amounts
* Very frequent betting activity
* Unusual odds usage
* Automated or bot-generated betting patterns

An automated system is required to identify such cases quickly and accurately.

---

## Solution

The proposed solution uses a machine learning model to analyze betting behavior and classify transactions as either:

* Normal
* Fraudulent

The entire process is executed through a real-time streaming architecture powered by FastAPI, Kafka, and Spark.

---

## System Architecture

Client / User

↓

FastAPI API

↓

Apache Kafka

↓

Apache Spark Streaming

↓

Machine Learning Model

↓

Fraud Detection Result

↓

Dashboard

---

## Technologies Used

### Backend

* Python
* FastAPI

### Stream Processing

* Apache Kafka
* Apache Spark Streaming

### Machine Learning

* Scikit-learn
* Random Forest Classifier
* Joblib

### Data Processing

* NumPy
* Pandas

### Visualization

* Flask Dashboard
* Matplotlib

### Cloud Services

* AWS S3
* AWS Lambda

---

## Data Flow

### Step 1

The user submits betting information through the API.

### Step 2

FastAPI validates the request and publishes the data to a Kafka topic.

### Step 3

Spark Streaming consumes the messages from Kafka.

### Step 4

The machine learning model evaluates the betting behavior.

### Step 5

The system calculates the fraud probability.

### Step 6

The results are displayed through the dashboard.

---

## Input Features

The machine learning model uses the following features:

* Bet Amount
* Time Between Bets
* Odds

---

## Example Input

```json
{
  "bet_amount": 1000,
  "time_between_bets": 3,
  "odds": 2.1
}
```

## Example Output

```json
{
  "fraud": 1,
  "fraud_probability": 0.92
}
```

---

## Key Features

* Real-time fraud detection
* Kafka-based event streaming
* Spark Streaming data processing
* Machine learning predictions
* REST API built with FastAPI
* Dashboard visualization
* AWS integration for file uploads

---

## Running the Project

### Start Kafka

```bash
cd C:\kafka
bin\windows\kafka-server-start.bat config\kraft\server.properties
```

### Start Spark Streaming

```bash
cd kafka_stream
python spark_job.py
```

### Start FastAPI

```bash
python -m uvicorn api.main:app --reload
```

### Start Dashboard

```bash
python dashboard/app.py
```

---

## API Example

### Endpoint

```http
POST /send
```

### Request

```json
{
  "bet_amount": 1000,
  "time_between_bets": 3,
  "odds": 2.1
}
```

### Response

```json
{
  "status": "sent to kafka"
}
```

---

## Benefits

* Automated fraud detection
* Real-time data processing
* Scalable distributed architecture
* Improved operational efficiency
* Enhanced platform security

---

## Future Improvements

* Deep learning-based fraud detection
* Real-time alerting system
* Advanced analytics dashboard
* Cloud-native deployment
* User behavior profiling

---

## Educational Value

This project demonstrates the integration of FastAPI, Apache Kafka, Apache Spark, and Machine Learning in a real-time distributed system. It provides practical experience with event-driven architectures, stream processing, and fraud detection techniques commonly used in modern data engineering and AI applications.
