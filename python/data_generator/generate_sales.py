import pandas as pd
import random
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_PATH = BASE_DIR / "data" / "raw"

customers = pd.read_csv(RAW_PATH / "customers.csv")
products = pd.read_csv(RAW_PATH / "products.csv")
stores = pd.read_csv(RAW_PATH / "stores.csv")
dates = pd.read_csv(RAW_PATH / "dates.csv")

discount_rules = {
    "Electronics": (5,15),
    "Fashion": (10,40),
    "Grocery": (0,5),
    "Beauty": (5,20),
    "Sports": (5,15),
    "Books": (0,10),
    "Toys": (5,15),
    "Home & Kitchen": (5,20)
}

quantity_rules = {
    "Electronics": (1,2),
    "Fashion": (1,4),
    "Grocery": (1,10),
    "Beauty": (1,5),
    "Sports": (1,2),
    "Books": (1,3),
    "Toys": (1,3),
    "Home & Kitchen": (1,2)
}

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

payment_weights = [45,25,15,10,5]

sales = []

for i in range(1,50001):

    customer = customers.sample(1).iloc[0]

    product = products.sample(1).iloc[0]

    store = stores.sample(1).iloc[0]

    date = dates.sample(1).iloc[0]

    category = product["category"]

    qty = random.randint(
        quantity_rules[category][0],
        quantity_rules[category][1]
    )

    discount_percent = random.uniform(
        discount_rules[category][0],
        discount_rules[category][1]
    )

    unit_price = product["unit_price"]

    gross_amount = qty * unit_price

    discount = round(
        gross_amount * discount_percent / 100,
        2
    )

    sales_amount = round(
        gross_amount - discount,
        2
    )

    sales.append({

        "sales_id":f"T{i:06}",

        "customer_id":customer["customer_id"],

        "product_id":product["product_id"],

        "store_id":store["store_id"],

        "date_key":date["date_key"],

        "quantity":qty,

        "unit_price":unit_price,

        "discount":discount,

        "sales_amount":sales_amount,

        "payment_method":random.choices(
            payment_methods,
            weights=payment_weights,
            k=1
        )[0]

    })

sales_df = pd.DataFrame(sales)

sales_df.to_csv(
    RAW_PATH/"sales.csv",
    index=False
)

print("="*60)
print("Sales Dataset Generated Successfully")
print("="*60)
print(sales_df.head())
print("="*60)