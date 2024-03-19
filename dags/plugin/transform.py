
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

        

