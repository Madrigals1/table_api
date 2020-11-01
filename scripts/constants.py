import os
from dotenv import load_dotenv

load_dotenv()

STATIC_PATH = os.environ.get("STATIC_PATH")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG")