import pandas as pd
from api.models import Property

def clean_number(value):
    if pd.isna(value):
        return 0
    if isinstance(value, str):
        value = value.replace(",", "").strip()
        if value == "":
            return 0
    try:
        return float(value)
    except:
        return 0

def import_excel():
    df = pd.read_excel("real_estate_data.xlsx")

    REQUIRED_FIELDS = [
        "final location", "year", "city",
        "loc_lat", "loc_lng",
        "total carpet area supplied (sqft)",
        "flat total", "shop total", "office total", "others total"
    ]

    for idx, row in df.iterrows():
        # Skip rows missing text fields
        if pd.isna(row["final location"]) or pd.isna(row["city"]):
            continue

        # Prepare known fields
        property_data = {
            "final_location": row["final location"],
            "year": int(row["year"]),
            "city": row["city"],
            "loc_lat": clean_number(row["loc_lat"]),
            "loc_lng": clean_number(row["loc_lng"]),
            "total_carpet_area": clean_number(row["total carpet area supplied (sqft)"]),
            "flat_total": int(clean_number(row["flat total"])),
            "shop_total": int(clean_number(row["shop total"])),
            "office_total": int(clean_number(row["office total"])),
            "others_total": int(clean_number(row["others total"])),
        }

        # Extra columns → Send to JSON
        extra_data = {}
        for col in df.columns:
            if col not in REQUIRED_FIELDS:
                extra_data[col] = row[col]

        property_data["extra_data"] = extra_]()_
