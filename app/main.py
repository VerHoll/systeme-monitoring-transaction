from fastapi import FastAPI
from kafka_producer import send_message_to_kafka

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Helloworld"}

@app.post("/send")
async def send_message(message: str):
    topic = "test-topic"
    send_message_to_kafka(topic, message)
    return {"status": "Message sent", "message": message, "topic": topic}

