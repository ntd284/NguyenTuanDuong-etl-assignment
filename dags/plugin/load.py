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
