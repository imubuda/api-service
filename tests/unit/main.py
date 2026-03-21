# main.py

import json
import logging
import os
import sys
from flask import Flask, request, jsonify
from api_service.config import Config
from api_service.database import Database
from api_service.routes import register_routes

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=Config.LOGGING_LEVEL,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def load_config():
    config = Config()
    config.load()
    return config

def init_database(config):
    db = Database(config)
    return db

def create_tables(db):
    db.create_tables()

def main():
    config = load_config()
    db = init_database(config)
    create_tables(db)
    register_routes(app)

    if __name__ == '__main__':
        app.run(host=config.HOST, port=config.PORT)

if __name__ == '__main__':
    main()