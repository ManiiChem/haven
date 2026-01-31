import os
from app import create_app
from config import DevelopmentConfig, ProductionConfig

env = os.getenv("FLASK_ENV", "production").lower()
config = ProductionConfig if env == "production" else DevelopmentConfig

app = create_app(config)

