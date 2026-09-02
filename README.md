# Automated CSV Data Processing & MongoDB Integration

## Overview

A Python-based ETL pipeline that automates the processing of customer CSV files, performs data cleaning and validation, generates cleaned output files, and stores processed data in MongoDB.

The project demonstrates automated file processing, data quality checks, database integration, logging, and output verification.

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

- Customer Contracts Link
- Customer Demo Link
- Customer Engagements Link
- Customer Contracts Link

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
Python
Pandas
MongoDB
PyMongo
Python-dotenv
CSV
ETL

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

## Data Processing

- The pipeline performs the following steps:

### 1. File Detection

- Automatically detects CSV files from the data directory.

### 2. Data Loading

- Loads CSV files into Pandas DataFrames.

### 3. Data Cleaning

The pipeline:

- Removes completely empty rows
- Removes duplicate records
- Converts numeric fields into appropriate numeric types
- Handles CSV encoding issues

### 4. Data Validation

- The pipeline checks for missing values and invalid numeric values.

### 5. Output Generation

- Cleaned datasets are saved in the output directory.

### 6. MongoDB Integration

- Processed records are stored in MongoDB using PyMongo.

The database contains the following collections:
```
customer_data_etl
│
├── customer_contracts
├── customer_demo
└── customer_engagements
```

### 8. Logging

Pipeline activities are recorded in:
```
logs/process.log
```

The cleaned output files were generated and the processed records were synchronized with MongoDB.

## Error Handling

The pipeline handles common processing issues such as:

CSV encoding errors
- Missing values
- Invalid numeric values
- MongoDB connection failures
- MongoDB insertion failures
- File processing errors

Errors and warnings are recorded in the application log for troubleshooting.

Output Verification

After processing each CSV file, the pipeline verifies that the cleaned output file has been successfully generated.

Author

Vaibhav Mahale
