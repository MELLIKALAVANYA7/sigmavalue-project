import pandas as pd
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Property

# Excel file path
file_path = 'real_estate_data.xlsx'
df = pd.read_excel(file_path)

for _, row in df.iterrows():
    # Standard fields
    property_data = {
        "final_location": row.get("final location"),
        "year": row.get("year"),
        "city": row.get("city"),
        "loc_lat": row.get("loc_lat"),
        "loc_lng": row.get("loc_lng"),
        "total_carpet_area": row.get("total carpet area supplied (sqft)"),
        "flat_total": row.get("flat total"),
        "shop_total": row.get("shop total"),
        "office_total": row.get("office total"),
        "others_total": row.get("others total")
    }

    # Extra columns stored in JSON
    extra_cols = {col: row[col] for col in df.columns if col not in property_data}
    property_data["extra_data"] = extra_cols

    Property.objects.create(**property_data)

print("All data imported successfully!")

