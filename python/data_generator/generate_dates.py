import pandas as pd
from pathlib import Path

# ------------------------------------
# Project Path
# ------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data" / "raw"

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# ------------------------------------
# Generate Date Range
# ------------------------------------

dates = pd.date_range(
    start="2023-01-01",
    end="2025-12-31",
    freq="D"
)

# ------------------------------------
# Create Date Dimension
# ------------------------------------

date_df = pd.DataFrame({

    "date_key": dates.strftime("%Y%m%d").astype(int),

    "full_date": dates,

    "day": dates.day,

    "month": dates.month,

    "month_name": dates.strftime("%B"),

    "quarter": dates.quarter,

    "year": dates.year,

    "weekday": dates.strftime("%A"),

    "week_number": dates.isocalendar().week,

    "is_weekend": dates.weekday >= 5

})

# ------------------------------------
# Save CSV
# ------------------------------------

date_df.to_csv(

    OUTPUT_PATH/"dates.csv",

    index=False

)

print(date_df.head())

print()

print("Date Dimension Generated Successfully")