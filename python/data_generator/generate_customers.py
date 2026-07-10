from faker import Faker
import pandas as pd
import random
from pathlib import Path

# ---------------------------------------
# Initialize Faker
# ---------------------------------------

fake = Faker("en_IN")

random.seed(42)

# ---------------------------------------
# Output Folder
# ---------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data" / "raw"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# ---------------------------------------
# Customer Segments
# ---------------------------------------

customer_segments = [
    "Regular",
    "Premium",
    "VIP"
]

segment_weights = [70, 20, 10]

# ---------------------------------------
# City-State Mapping
# ---------------------------------------

locations = {
    "Hyderabad": "Telangana",
    "Warangal": "Telangana",
    "Bengaluru": "Karnataka",
    "Mysuru": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Coimbatore": "Tamil Nadu",
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Surat": "Gujarat",
    "Delhi": "Delhi",
    "Lucknow": "Uttar Pradesh",
    "Kanpur": "Uttar Pradesh",
    "Kolkata": "West Bengal",
    "Jaipur": "Rajasthan",
    "Kochi": "Kerala"
}

# ---------------------------------------
# Generate Customers
# ---------------------------------------

customers = []

for i in range(1, 5001):

    city = random.choice(list(locations.keys()))

    customer = {

        "customer_id": f"C{i:05}",

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "gender": random.choice(["Male", "Female"]),

        "age": random.randint(18, 70),

        "city": city,

        "state": locations[city],

        "join_date": fake.date_between(
            start_date="-4y",
            end_date="today"
        ),

        "customer_segment": random.choices(
            customer_segments,
            weights=segment_weights,
            k=1
        )[0]
    }

    customers.append(customer)

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

customer_df = pd.DataFrame(customers)

# ---------------------------------------
# Save CSV
# ---------------------------------------

customer_df.to_csv(
    OUTPUT_PATH / "customers.csv",
    index=False
)

print("=" * 60)
print("Customer Dataset Generated Successfully")
print("=" * 60)
print(f"Total Records : {len(customer_df)}")
print(f"Location      : {OUTPUT_PATH}")
print("=" * 60)