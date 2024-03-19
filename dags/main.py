from plugin.transform import transform
from plugin.load import load_mysql
from plugin.extract import extract


def run_etl_process():
    # Step 1: Extract
    # extracted_data = extract.main()
    
    # Step 2: Transform
    # transformed_data = transform.transform()
    
    # Step 3: Load
    load_data_mysql = load_mysql.backup_mysql()
    
    print("ETL Process Completed Successfully")

if __name__ == "__main__":
    run_etl_process()