#Transform file reads the parquet bronze file, cleans it by changing the datatypes of some columns such as goals, minutes and assists
import pandas as pd 
import os 
import glob

def transform():
   files = glob.glob("Data/Bronze/*.parquet")
   newest_file = max(files, key= os.path.getctime)
   df = pd.read_parquet(newest_file)

   df = df.rename(columns= {'id': 'player_id'})

   df['season'] = 2024

   df = df.drop_duplicates(subset= 'player_id')

   df['goals'] = df['goals'].astype(int)
   df['assists'] = df['assists'].astype(int)
   df['minutes'] = df['minutes'].astype(int)

   df.to_parquet(f"Data/Silver/topscorers_clean.parquet", index= False)
   print('\n')

   print("Saved to Silver")
   print('\n')

   print(df.dtypes)