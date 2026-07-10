import pandas as pd
import random
from pathlib import Path

random.seed(42)

# -----------------------------------
# Project Path
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# -----------------------------------
# City Information
# -----------------------------------

locations = [
    ("Hyderabad","Telangana","South"),
    ("Warangal","Telangana","South"),
    ("Bengaluru","Karnataka","South"),
    ("Mysuru","Karnataka","South"),
    ("Chennai","Tamil Nadu","South"),
    ("Coimbatore","Tamil Nadu","South"),
    ("Mumbai","Maharashtra","West"),
    ("Pune","Maharashtra","West"),
    ("Ahmedabad","Gujarat","West"),
    ("Surat","Gujarat","West"),
    ("Delhi","Delhi","North"),
    ("Lucknow","Uttar Pradesh","North"),
    ("Kanpur","Uttar Pradesh","North"),
    ("Jaipur","Rajasthan","North"),
    ("Kolkata","West Bengal","East"),
    ("Kochi","Kerala","South")
]

stores = []

for i in range(1,121):

    city,state,region = random.choice(locations)

    stores.append({

        "store_id":f"S{i:03}",

        "store_name":f"RetailMart {city} Branch {i}",

        "city":city,

        "state":state,

        "region":region

    })

df = pd.DataFrame(stores)

df.to_csv(

    OUTPUT_PATH/"stores.csv",

    index=False

)

print(df.head())

print()

print("Stores Generated Successfully")