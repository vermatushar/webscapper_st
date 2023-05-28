from selenium import webdriver
import pandas as pd
import sys
from datetime import datetime as dt

# URL from where the tables will be scraped
#URL = 'https://chartink.com/screener/strong-move-range-break-out-with-volume-and-obv-75min'
URL = 'https://chartink.com/screener/strong-stocks'


# define driver as firefox webdriver
driver = webdriver.Safari()

# loads the page in firefox
driver.get(URL)


# Column names
col_tag = driver.find_element('xpath', '//*[@id="DataTables_Table_0"]/thead')
cols_th = col_tag.find_elements('tag name', 'th')
cols_list = []
for col_th in cols_th:
    cols_list.append(col_th.text)

print(cols_list)
# get the html element at a specific xpath
element = driver.find_element('xpath', '//*[@id="DataTables_Table_0"]/tbody')
# print(element)
# extract the html from that element
# //*[@id="DataTables_Table_0"]/tbody/tr[1]/td[2]/a
rows = element.find_elements('tag name', 'tr')
rows_list = []
for row in rows:
    values = row.find_elements('tag name', 'td')
    row_list = []
    for val in values:
        # print(val.text)
        row_list.append(val.text)
    rows_list.append(row_list)
print(rows_list)


# creating dataframe
df = pd.DataFrame(columns=cols_list, data=rows_list)
df['Timestamp'] = dt.now()
df = df.drop('Sr.', axis=1)
df.index += 1
print(df)





# Use try except block to extract the tables from html and to catch the exception gracefully if the table doesnot exist
try:
    # Read all tables in the response into a list of dataframes
    # dataframes = pd.read_html(element_html)

    # close the browser / webdriver
    driver.close()

# Incase no table is found print "No table found" and exit gracefully
except:
    print("No table found")

    # close the browser / webdriver
    driver.close()

    # exit program
    sys.exit(0)

# Iterate through the data frames to access each table
# for dataframe in dataframes:
# print(dataframe)