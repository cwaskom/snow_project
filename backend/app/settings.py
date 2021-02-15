import os
from dotenv import load_dotenv

load_dotenv()

RECIPIENTS = os.getenv("RECIPIENTS")
API_KEY = os.getenv("API_KEY")
