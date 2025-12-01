import pandas as pd
import os
import django
from django.db import connection

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Property

file_path = 'real_estate_data.xlsx'
df = pd.read_excel(file_path)

# Function to check if a column exists in the table
def column_exists(table_name, column_name):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_name=%s AND column_name=%s",
            [table_name, column_name]
        )
        return cursor.fetchone() is not None

# Add missing columns dynamically (only supports simple types)
for col in df.columns:
    field_name = col.replace(" ", "_")
    if not column_exists("api_property", field_name):
        with connection.cursor() as cursor:
            cursor.execute(f'ALTER TABLE api_property ADD COLUMN "{field_name}" text;')  # Using text type for simplicity

# Insert all rows
for _, row in df.iterrows():
    row_data = {col.replace(" ", "_"): str(row[col]) for col in df.columns}
    Property.objects.create(**row_data)

print("All data imported dynamically!")
