from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_PATH = BASE_DIR / "data" / "raw"

customers = pd.read_csv(RAW_PATH / "customers.csv")
products = pd.read_csv(RAW_PATH / "products.csv")
stores = pd.read_csv(RAW_PATH / "stores.csv")
dates = pd.read_csv(RAW_PATH / "dates.csv")
sales = pd.read_csv(RAW_PATH / "sales.csv")


def validate_duplicates(df, column_name):
    duplicates = df[column_name].duplicated().sum()
    print(f"{column_name}: {duplicates} duplicate(s)")


print("=" * 60)
print("CUSTOMER VALIDATION")
print("=" * 60)
validate_duplicates(customers, "customer_id")

print("\nPRODUCT VALIDATION")
print("=" * 60)
validate_duplicates(products, "product_id")

print("\nSTORE VALIDATION")
print("=" * 60)
validate_duplicates(stores, "store_id")

print("\nDATE VALIDATION")
print("=" * 60)
validate_duplicates(dates, "date_key")

print("\nSALES VALIDATION")
print("=" * 60)
validate_duplicates(sales, "sales_id")

print("\nMissing Values")
print("=" * 60)
print(sales.isnull().sum())