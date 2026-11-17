
# Demo Flask Service

โปรเจกต์ Machine Learning Model as a Service
โดยใช้ Flask และ Docker

## Project Structure

- app.py
- train_model.py
- requirements.txt
- Dockerfile
- templates/main.html
- model/model.pkl

## Installation

pip install -r requirements.txt

## Train Model

python train_model.py

## Run Flask

python app.py

## Run with Docker

docker build -t demo-flask-service .

docker run -p 5000:5000 demo-flask-service
