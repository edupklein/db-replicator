# 🗄️ Kafka Docker Images

This docker compose file creates 3 images for Kafka, Kafka-ui and Zookeeper.
- Kafka:
    - External port: 9093
    - Internal port: 9092

- Zookeeper:
    - Client port: 2181

- Kafka-ui:
    - Port: 8085

## 🚀 Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/edupklein/db-replicator.git
    ```
1. Navigate to the project directory:
    ```bash
    cd dbr-kafka
    ```
1. Run docker the docker image:
    ```bash
    docker compose up -d
    ```