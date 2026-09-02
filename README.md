# Automated CSV Data Processing & MongoDB Integration

## Overview

A Python-based ETL pipeline that automates the processing of  CSV files, performs data cleaning and validation, generates cleaned output files, and stores processed data in MongoDB.

The project demonstrates automated file processing, data quality checks, database integration, and output verification.

## Features

- Automatic CSV file detection
- CSV processing using Pandas
- Duplicate record removal
- Missing value detection
- Basic data validation
- Cleaned CSV output generation
- Output file verification
- Error handling

## ETL Workflow

```
CSV Files
    ↓
File Detection
    ↓
Pandas Data Loading
    ↓
Data Cleaning
    ↓
Data Validation
    ↓
Cleaned CSV Output
    ↓
MongoDB
    ↓
Execution Log 
```

## Dataset

The pipeline processes three customer-related CSV datasets:

- Customer Contracts [Link](https://github.com/VaibhavM1122/Automated-CSV-Data-Processing-MongoDB/blob/main/data/Customer%20Contracts%24.csv)
- Customer Demo [Link](https://github.com/VaibhavM1122/Automated-CSV-Data-Processing-MongoDB/blob/main/data/Customer%20Demo.csv)
- Customer Engagements [Link](https://github.com/VaibhavM1122/Automated-CSV-Data-Processing-MongoDB/blob/main/data/Customer%20Engagements.csv)

## Project Structure

```
Automated-CSV-Data-Processing-MongoDB
│
├── data
│   ├── Customer Contracts$.csv
│   ├── Customer Demo.csv
│   └── Customer Engagements.csv
│
├── output
│   ├── customer_contracts_cleaned.csv
│   ├── customer_demo_cleaned.csv
│   └── customer_engagements_cleaned.csv
│
├── logs
│   └── process.log
│
├── src
│   ├── main.py
│   ├── data_cleaning.py
│   ├── mongodb_connection.py
│   └── logger.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies Used
- Python
- Pandas
- MongoDB
- PyMongo
- Python-dotenv
- CSV
- ETL

## Installation

Install the required dependencies:

```
pip install -r requirements.txt
```

## MongoDB Configuration
```
Create a .env file in the project root:
MONGO_URI=mongodb:
DATABASE_NAME=customer_data
```

Running the Pipeline

- Run the following command from the project root:
```
python src/main.py
```
