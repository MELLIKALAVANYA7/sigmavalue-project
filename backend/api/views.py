from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import os

# Make sure your Excel file is in the backend folder
DATA_FILE = os.path.join(os.path.dirname(__file__), '../real_estate_data.xlsx')

# Load Excel data
df = pd.read_excel(DATA_FILE)

@api_view(['POST'])
def analyze_area(request):
    """
    Expects JSON: {"area": "Wakad"}
    Returns: summary, chart data, filtered table
    """
    area = request.data.get('area')
    if not area:
        return Response({"error": "Area not provided"}, status=400)
    
    # Filter data by area (case-insensitive)
    filtered = df[df['Area'].str.lower() == area.lower()]
    if filtered.empty:
        return Response({"error": "No data found for this area"}, status=404)
    
    # Mock summary
    summary = f"Analysis for {area}: Average price {filtered['Price'].mean():.2f}, Average demand {filtered['Demand'].mean():.2f}"

    # Chart data: Price & Demand per Year
    chart_data = filtered.groupby('Year')[['Price', 'Demand']].mean().reset_index().to_dict(orient='records')

    # Filtered table as list of dicts
    table_data = filtered.to_dict(orient='records')

    return Response({
        "summary": summary,
        "chart_data": chart_data,
        "table_data": table_data
    })

