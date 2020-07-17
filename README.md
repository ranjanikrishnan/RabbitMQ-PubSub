# RabbitMQ PubSub

Topic based publish-subscribe implementation which includes a producer and a consumer. The communication between the producer and consumer is handled by RabbitMQ, which is a message broker (using AMQP protocol).

The workflow is as follows:
- Data extracted from csv file
- Extracted data sent to producer 
- Producer publishes data to a queue
- Consumer listening to the queue
- Consumer consumes the message
- Message put in postgres

### Prerequisites

- Docker
- Docker Compose

### Project Setup

```
docker-compose up
```

### Execute tests

```
cd consumer
python -m pytest tests/
```

