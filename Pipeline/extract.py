#Extract extrai dados do API, desfaz o nested JSON e salva em formato parquet
import requests
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

def extract():
    load_dotenv()

    url = "https://v3.football.api-sports.io/players/topscorers"
    api_key = os.getenv("API_KEY")

    params = {
        "league": 39,
        "season": 2024
    }
    headers = {
        "x-apisports-key": api_key
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    new_data = []
    
     #Separacao de dados
    if response.status_code == 200:
        for player in data['response']:
            flat_dict = {
                'id'          : player['player']['id'],
                'name'        : player['player']['name'],
                'team'        : player['statistics'][0]['team']['name'],
                'goals'       : player['statistics'][0]['goals']['total'],
                'assists'     : player['statistics'][0]['goals']['assists'],
                'minutes'     : player['statistics'][0]['games']['minutes'],
                'yellow_cards': player['statistics'][0]['cards']['yellow'],
                'red_cards'   : player['statistics'][0]['cards']['red']
            }
            new_data.append(flat_dict)

        df = pd.DataFrame(new_data)
        load_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        df.to_parquet(f"Data/Bronze/topscorers_{load_id}.parquet", index=False)
        print(f"Saved to Data/Bronze/topscorers_{load_id}.parquet")
    else:
        print(response.status_code)
        raise Exception("Status is not 200")