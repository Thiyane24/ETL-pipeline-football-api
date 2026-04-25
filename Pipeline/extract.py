import requests
import os
from dotenv import load_dotenv


url = "https://v3.football.api-sports.io/leagues"
load_dotenv()
api_key= os.getenv("API_KEY")

