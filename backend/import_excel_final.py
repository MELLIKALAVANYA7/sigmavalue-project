import pandas as pd
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Property

# Path to your Excel file
file_path = 'real_estate_data.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Loop through each row and insert into database
for _, row in df.iterrows():
    Property.objects.create(
        final_location=row['final location'],
        year=row['year'],
        city=row['city'],
        loc_lat=row['loc_lat'],
        loc_lng=row['loc_lng'],
        total_carpet_area=row['total carpet area supplied (sqft)'],
        flat_total=row['flat total'],
        shop_total=row['shop total'],
        office_total=row['office total'],
        others_total=row['others total']
    )

print("All data imported successfully!")
