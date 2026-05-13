# Real-Time IOT Data Pipeline Project - MongoDB

## Project Overview

This project is a real-time IoT streaming data pipeline built using modern data engineering tools and architectures.

The pipeline collects live IoT sensor data from the ThingSpeak API, streams the data through Apache Kafka, processes the streaming events using Python consumers, and stores the raw events inside MongoDB.

The goal of this project is to simulate a real-world streaming data engineering pipeline that can later be extended with:
- Airbyte for ingestion
- Snowflake as a cloud data warehouse
- dbt for data transformations and analytics engineering

---

# Architecture

```text
ThingSpeak API
       ↓
Python Producer
       ↓
Apache Kafka
       ↓
Python Consumer
       ↓
MongoDB
```

---

# Current Pipeline Flow

1. Fetch live IoT sensor data from the ThingSpeak API
2. Serialize data into JSON format
3. Stream events into Kafka topic (`sensor_data`)
4. Consume Kafka messages using a Python consumer
5. Store streaming events inside MongoDB

---

# Tech Stack

- Apache Kafka
- Kafka UI
- Python
- MongoDB
- Mongo Express
- Docker
- Docker Compose
- WSL Ubuntu
- Git & GitHub

### Upcoming Technologies

- Airbyte
- Snowflake
- dbt

---

# Project Structure

```text
realtime-iot-project/
│
├── consumer/
│   └── consumer.py
│
├── producer/
│   └── producer.py
│
├── docker-compose.yml
├── README.md
├── .gitignore
└── venv/


```
<img width="826" height="260" alt="image" src="https://github.com/user-attachments/assets/02ed2305-da08-404d-bb01-f3762746f4ae" />

---

# Docker Services

The project uses Docker Compose to orchestrate all services.

Current services:
- Kafka
- Kafka UI
- MongoDB
- Mongo Express

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Abeer-omar/Real-Time-IOT-Data-Pipeline-Project-MongoDB.git

cd Real-Time-IOT-Data-Pipeline-Project-MongoDB
```

---

## 2. Start Docker Services

```bash
docker compose up -d
```

---

## 3. Access Services

### Kafka UI

```text
http://YOUR_IP:12000
```

---

### Mongo Express

```text
http://YOUR_IP:8081
```

---

### MongoDB Compass Connection

```text
mongodb://YOUR_IP:27017/
```

---

# Kafka Topic Creation

Create Kafka topic:

```bash
docker exec kafka kafka-topics.sh \
--create \
--topic sensor_data \
--bootstrap-server localhost:9092
```

Verify topic exists:

```bash
docker exec kafka kafka-topics.sh \
--list \
--bootstrap-server localhost:9092
```


---

# Python Environment Setup

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install required libraries:

```bash
pip install kafka-python requests pymongo
```

---

# Producer Layer

The producer fetches live IoT sensor data from the ThingSpeak API and streams the events into Kafka.

## Producer Responsibilities

- Fetch API data
- Convert data into JSON
- Serialize JSON into bytes
- Send messages to the Kafka topic
- Stream continuously every 5 seconds

---

# Producer Code

Location:

```text
producer/producer.py
```

---

# Consumer Layer

The consumer reads Kafka streaming events and stores them inside MongoDB.

## Consumer Responsibilities

- Read Kafka messages
- Deserialize JSON events
- Insert documents into MongoDB
- Continuously process real-time events

---

# Consumer Code

Location:

```text
consumer/consumer.py
```

---

# Kafka UI


<img width="1912" height="516" alt="kafka1" src="https://github.com/user-attachments/assets/a723e336-c405-4f4a-b3e9-c82dca43273d" />

<img width="1911" height="632" alt="kafka2" src="https://github.com/user-attachments/assets/85451efa-6217-48fc-9a74-85e6d5bd5389" />

<img width="1652" height="825" alt="kafka3" src="https://github.com/user-attachments/assets/43a4810e-7f87-4a2e-96ce-d7eed0589338" />



---

# Mongo Express UI



<img width="1471" height="861" alt="Mongo Express" src="https://github.com/user-attachments/assets/20e8ae7c-4eab-4f10-9b4a-a3013360d683" />


---

# Current Architecture Notes

At this stage:

- Kafka acts as the streaming buffer and message broker
- MongoDB acts as the raw operational data store

Future architecture will include:

```text
MongoDB
    ↓
Airbyte
    ↓
Snowflake
    ↓
dbt
    ↓
Analytics / Dashboards
```

---

# Key Data Engineering Concepts Used

| Concept | Purpose |
|---|---|
| API | Source of IoT sensor data |
| Kafka Producer | Streams real-time events |
| Kafka Topic | Stores streaming events |
| Kafka Consumer | Processes streaming data |
| JSON Serialization | Standardized event format |
| MongoDB | Raw document storage |
| Docker | Containerized infrastructure |
| Streaming Pipeline | Real-time data processing |

---

# Future Improvements

- Add Airbyte for ingestion
- Integrate Snowflake data warehouse
- Build dbt transformation models
- Add orchestration with Airflow
- Create analytics dashboards
- Add monitoring and logging
- Deploy pipeline to cloud infrastructure

---

# Author

Abeer Omar

GitHub Repository:

https://github.com/Abeer-omar/Real-Time-IOT-Data-Pipeline-Project-MongoDB
