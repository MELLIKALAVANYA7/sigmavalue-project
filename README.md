# SigmaValue Project

## Description
SigmaValue is a real estate data processing project. It uses Python scripts to import and process Excel files containing real estate data, generate charts, and provide visual insights. The project demonstrates data handling, analysis, and visualization in a structured and efficient way.

## Features
- Import Excel data from multiple formats
- Process and clean real estate data
- Generate charts and visualizations for analysis
- Optional integration with language models (LLM) for data insights
- Easy-to-run Python scripts

## Project Structure
sigmavalue-project/
│
├── backend/ # Python scripts and Excel files
│ ├── import_excel.py
│ ├── import_excel_auto.py
│ ├── import_excel_auto_all.py
│ ├── import_excel_dynamic.py
│ ├── import_excel_final.py
│ ├── import_final.py
│ ├── manage.py
│ ├── read_excel.py
│ └── real_estate_data.xlsx
│
├── requirements.txt # Project dependencies
├── README.md # Project overview
└── .gitignore # Files/folders ignored by Git


## How to Run
1. Clone the repository:

```bash
git clone https://github.com/MELLIKALAVANYA7/sigmavalue-project.git
cd sigmavalue-project


Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows


Install dependencies:

pip install -r requirements.txt


Run the scripts from the backend/ folder, for example:

python backend/import_excel.py


Make sure real_estate_data.xlsx is present in the backend/ folder.
