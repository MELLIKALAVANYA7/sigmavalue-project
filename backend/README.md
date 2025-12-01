# Real Estate Django Assignment

## Project Description
This is a Django-based project that imports real estate data from an Excel file and stores it in a database. The admin can view, manage, and add property records via the Django admin interface. The project also supports dynamic handling of extra Excel columns.

---

## Features
- Import property data from `real_estate_data.xlsx` using a Python script.
- Store standard fields in the database (location, year, city, carpet area, flat/shop/office/other totals).
- Automatically stores any extra Excel columns in a JSON field (`extra_data`).
- Manage properties via Django admin.

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone <your-github-repo-url>
cd sigmavalue-project/backend
