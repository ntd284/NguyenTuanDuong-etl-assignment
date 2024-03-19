# ETL Pipeline for Candidate Profile Data

## Project Structure Overview

This project implements an Extract, Transform, Load (ETL) pipeline specifically designed for the extraction and transformation of candidate profile data from various sources. Below is an outline of the project directory structure and a description of each component:

## Directory Structure

NGUYENTUANDUONG-ETL-ASSIGNMENT/
├── dags/
│   └── [DAG definition files]
├── file/
│   ├── list_candidate.txt          # A list of candidates to process
│   ├── login_credential.txt        # Credentials for sources requiring authentication
│   ├── output.csv                  # Final output after ETL process
│   ├── profiles-formatted.csv      # Profiles after transformation
│   └── profiles-raw.csv            # Raw profile data extracted from sources
├── plugin/
│   ├── function/
│   │   ├── credentials.json        # JSON file containing additional credentials
│   │   ├── filepath.py             # Utility functions for file path handling
│   │   └── operation.py            # Utility functions for common operations
│   ├── extract.py                  # Script to extract data from sources
│   ├── load.py                     # Script to load data into the desired storage
│   ├── transform.py                # Script to transform raw data into a structured format
│   └── main.py                     # Main script to orchestrate the ETL pipeline
├── README.md                       # Documentation and instructions
└── requirements.txt                # Python dependencies required

## Key Components

- dags/: Contains Airflow DAG definitions that schedule and monitor the ETL process.
    - file/: Holds input files such as candidate lists, login credentials, and outputs from the ETL steps.
    - plugin/: Includes the core Python scripts and utility functions for the ETL process:
    - function/: Contains credentials.json for configuration, filepath.py for path handling, and operation.py for common - - operational functions.
    - extract.py: Entry point for the extraction process, responsible for sourcing data from various platforms.
    - transform.py: Processes the raw data, normalizes, and enriches it according to the specified data schema.
    - load.py: Manages the persistence of transformed data into the final storage or file format.
main.py: Orchestrates the ETL pipeline by calling extract, transform, and load functions in order.

## Getting Started
- <b>Install the dependencies:</b>

```

```
