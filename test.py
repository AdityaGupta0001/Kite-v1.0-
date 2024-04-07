import pandas as pd
from sqlalchemy import create_engine

csv_file = '/Users/manayapachpor/Downloads/iata-icao.csv'

engine = create_engine('mysql+mysqlconnector://root:Kastu0308@localhost/dbms')

df = pd.read_csv(csv_file, encoding='ISO-8859-1')

table_name = 'airports'

df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print("CSV file imported into MySQL database.")
