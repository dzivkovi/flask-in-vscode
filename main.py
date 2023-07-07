# Inspired by https://code.visualstudio.com/docs/python/tutorial-flask

# Can be tested from the VScode or command line without having to deply the code to GCP.
# To run from command line:
#   $ python -m flask run --port 5000

import logging
import os
from flask import Flask

import google.cloud.logging
from dotenv import load_dotenv

import business_logic

# Load environment variables
load_dotenv()

if __name__ != '__main__':
    # Setup GCP logging
    client = google.cloud.logging.Client()
    # Configure the default logger to use the logging client
    # By default this captures all logs at INFO level and higher
    client.setup_logging()
    # Adjust the logging level as per the environment variable
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    logging.basicConfig(level=LOG_LEVEL)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>", methods=["POST", "GET"])
def hello_there(name):
    # do not place business logic in the route functions
    return business_logic.greeting(name)

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", '8080'))

    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run. See entrypoint in Dockerfile.
    app.run(host="127.0.0.1", port=PORT, debug=True)
