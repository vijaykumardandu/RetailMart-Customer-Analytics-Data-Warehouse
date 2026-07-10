import pandas as pd
import random
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data" / "raw"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

product_catalog = {
    "Electronics": {
        "Mobile": ["Samsung Galaxy A55", "iPhone 15", "OnePlus 13"],
        "Laptop": ["Dell Inspiron", "HP Pavilion", "Lenovo ThinkPad"],
        "Tablet": ["iPad Air", "Samsung Tab S9", "Lenovo Tab P12"]
    },
    "Fashion": {
        "Shirts": ["Formal Shirt", "Casual Shirt", "Linen Shirt"],
        "Jeans": ["Slim Fit Jeans", "Regular Jeans", "Denim Jeans"],
        "Shoes": ["Running Shoes", "Sneakers", "Sports Shoes"]
    },
    "Grocery": {
        "Rice": ["Basmati Rice", "Sona Masoori Rice"],
        "Oil": ["Sunflower Oil", "Groundnut Oil"],
        "Snacks": ["Potato Chips", "Namkeen"]
    },
    "Home & Kitchen": {
        "Mixer": ["Mixer Grinder"],
        "Cooker": ["Pressure Cooker"],
        "Furniture": ["Office Chair", "Study Table"]
    },
    "Beauty": {
        "Shampoo": ["Dove Shampoo", "Clinic Plus"],
        "Soap": ["Lux Soap", "Pears Soap"],
        "Face Wash": ["Himalaya Face Wash"]
    },
    "Sports": {
        "Cricket": ["Cricket Bat", "Cricket Ball"],
        "Football": ["Football"],
        "Gym": ["Dumbbell Set"]
    },
    "Books": {
        "Fiction": ["The Alchemist", "Atomic Habits"],
        "Education": ["Python Programming", "SQL Fundamentals"]
    },
    "Toys": {
        "Educational": ["Puzzle Game"],
        "Indoor": ["Chess Board"]
    }
}

brands = [
    "Samsung","Apple","Dell","HP","Lenovo",
    "Sony","Nike","Adidas","Puma","LG",
    "Boat","Philips","Prestige","Milton",
    "Dove","Nivea"
]

price_ranges = {
    "Electronics": (5000,120000),
    "Fashion": (300,5000),
    "Grocery": (50,1000),
    "Home & Kitchen": (500,25000),
    "Beauty": (100,2000),
    "Sports": (400,15000),
    "Books": (200,2000),
    "Toys": (250,5000)
}

products = []

for i in range(1,501):

    category = random.choice(list(product_catalog.keys()))

    sub_category = random.choice(
        list(product_catalog[category].keys())
    )

    product_name = random.choice(
        product_catalog[category][sub_category]
    )

    min_price,max_price = price_ranges[category]

    products.append({

        "product_id":f"P{i:04}",

        "product_name":product_name,

        "category":category,

        "sub_category":sub_category,

        "brand":random.choice(brands),

        "unit_price":round(
            random.uniform(min_price,max_price),2
        )
    })

df = pd.DataFrame(products)

df.to_csv(
    OUTPUT_PATH/"products.csv",
    index=False
)

print(df.head())
print()
print("Products Generated Successfully")