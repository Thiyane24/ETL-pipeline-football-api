from Pipeline.extract import extract
from Pipeline.transform import transform
from Pipeline.load import load
from datetime import datetime



print(f"Starting Pipeline at {datetime.now()}")

extract()
transform()
load()
print("Pipeline executed...")
