# ETL Pipeline for Candidate Profile Data

## Project Structure Overview

This project implements an Extract, Transform, Load (ETL) pipeline specifically designed for the extraction and transformation of candidate profile data from various sources. Below is an outline of the project directory structure and a description of each component:

## Directory Structure
```
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
```
## Key Components

- <b>dags/</b>: Contains Airflow DAG definitions that schedule and monitor the ETL process.
    - <b>file/</b>: Holds input files such as candidate lists, login credentials, and outputs from the ETL steps.
    - <b>plugin/</b>: Includes the core Python scripts and utility functions for the ETL process:
    - <b>function/</b>: Contains credentials.json for configuration, filepath.py for path handling, and operation.py for common - - operational functions.
    - <b>extract.py</b>: Entry point for the extraction process, responsible for sourcing data from various platforms.
    - <b>transform.py</b>: Processes the raw data, normalizes, and enriches it according to the specified data schema.
    - <b>load.py</b>: Manages the persistence of transformed data into the final storage or file format.
main.py: Orchestrates the ETL pipeline by calling extract, transform, and load functions in order.

## Getting Started
- <b>Install the dependencies:</b>
```
https://github.com/ntd284/NguyenTuanDuong-etl-assignment.git
```

- <b>Modify directory of filepath in `filepath.py`</b>
```
import os
class conf():
def filepath_credentials():
    return '{here}/NguyenTuanDuong-etl-assignment/keys/credentials.json'
def filepath():
    return '{here}/NguyenTuanDuong-etl-assignment/dags/file'
```
- <b> Navigate to the `src/` directory and run:</b>
```
python3 main.py //This will execute the entire ETL pipeline.
```

## Code Snippet:

<b>1. Data Extraction (extract.py) </b>
This script is responsible for crawling data from predefined web sources.

```
class extract():
    def main():
        with open(f'{conf.filepath()}/login_credential.txt',"r",encoding="utf-8") as outfile:
            lst_accs = outfile.read().split()
            num_of_page = 2
            title = "Software Engineer"
            print(f'save_profile_tag - number of page: {num_of_page}')
            for lst_ac in lst_accs:
                chrome_version = '114.0.5735.90'
                username = lst_ac.split(':')[0]
                password = lst_ac.split(':')[1]
                options = webdriver.ChromeOptions()
                options.add_argument("--incognito")
                options.add_argument("--headless")
                driver = webdriver.Chrome(options=options)
    
                wait = WebDriverWait(driver, 5)
                url = 'https://www.linkedin.com'
                driver.get(url)
                opera.login(driver,username,password)
                opera.search(wait,title,driver)
                opera.get_all_url_on_pages(conf.filepath(),driver,wait,num_of_page)
                opera.scan(conf.filepath(),driver,wait)

```

<b>2. Data Transformation (transform.py)</b>
After extraction, data often needs to be cleaned or restructured.

```
import csv
import pandas as pd
from plugin.function.filepath import conf

class transform():
    def extract_urls(urls):
        url_list = urls.strip("[]").replace("'", "").split(", ")
        linkedin = [url for url in url_list if 'linkedin.com' in url]
        github = [url for url in url_list if 'github.com' in url]
        medium = [url for url in url_list if 'medium.com' in url]
        other = [url for url in url_list if 'linkedin.com' not in url and 'github.com' not in url and 'medium.com' not in url]
        return pd.Series({'URL_LinkedIn': linkedin, 'URL_GitHub': github, 'URL_Medium': medium, 'URL_Other': other})
    def transform():
        df = pd.read_csv(conf.filepath() + '/profiles-raw.csv')
        url_columns = df['URL'].apply(transform.extract_urls)
        df = pd.concat([df, url_columns], axis=1)
        df = df.drop('URL', axis=1)
        df.to_csv(conf.filepath() + '/profiles-formated.csv', index=False)
        print(df)  # This will print the first 5 rows of the DataFrame

```

<b>3. Data Loading (load.py)</b>
This script saves the transformed data to a file or database.
```
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from plugin.function.filepath import conf
class load_mysql():
    def backup_mysql():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nokia55301",
        database="schemaprofiles"
        )
        mycursor = mydb.cursor()

        mycursor.execute("DROP TABLE IF EXISTS profiles")

        mycursor.execute(""" 
                        CREATE TABLE IF NOT EXISTS profiles(id 
                        INT AUTO_INCREMENT PRIMARY KEY, 
                        Name VARCHAR(255), 
                        Job VARCHAR(255),
                        Location VARCHAR(255),
                        Experience TEXT,
                        URL_LinkedIn VARCHAR(255),
                        URL_Github VARCHAR(255),
                        URL_Medium VARCHAR(255),
                        URL_Other VARCHAR(255))""")
        engine = create_engine("mysql+mysqlconnector://root:Nokia55301@localhost:3306/schemaprofiles",connect_args={'charset':'utf8'})
        df = pd.read_csv(f'{conf.filepath()}/profiles-formated.csv')
        df.to_sql('profiles', con=engine, if_exists='append', index=False)
        print(df)
        print('')

```