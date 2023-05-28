import pandas as pd
import sqlite3
from mpages import *

conn = sqlite3.connect('master_db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS mastertable (Sr integer,StockName text,Symbol text ,Links text ,PChg float,Price float ,Volume integer,tstamp timestamp)')
conn.commit()
old_df = pd.read_csv('./data/master.csv')
old_df.to_sql('mastertable', conn, if_exists='replace', index=False)
c.close()

'''
# Fetch all the rows returned by the query
rows = c.fetchall()

# Process the rows as needed
for row in rows:
    print(row)

# Close the connection
'''
#conn.close()
