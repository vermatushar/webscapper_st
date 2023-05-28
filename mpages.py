from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys
from datetime import datetime as dt
import time
import os
from config import *


#print("Initialising program")
old_df = None
count = 1
COLUMNS = None


def create_dir(directory_path):
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            # Create the directory
            os.makedirs(directory_path)
            print("Directory created successfully.")
        else:
            pass
    except Exception as ex:
        pass


def dataframer(cols_list, rows_list):
    df = pd.DataFrame(columns=cols_list, data=rows_list)
    df['Timestamp'] = dt.now()
    return df


def df_appender(old_df, new_df):
    old_df = pd.concat([old_df, new_df], ignore_index=True)
    return old_df


def page_table(driver):
    global COLUMNS
    col_tag = driver.find_element('xpath', '//*[@id="DataTables_Table_0"]/thead')
    cols_th = col_tag.find_elements('tag name', 'th')
    cols_list = []
    for col_th in cols_th:
        cols_list.append(col_th.text)

    #print(cols_list)
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
    #print(rows_list)
    df = dataframer(cols_list, rows_list)
    COLUMNS = tuple(cols_list)
    return df


def paginator(driver):
    global old_df, count
    time.sleep(3)
    next_page = driver.find_element("partial link text", 'Next')
    next_page_runner = driver.find_element("class name", 'paginate_button.next')
    #print(next_page)
    val = str(next_page_runner.get_attribute('class'))
    #print(val)
    #print(next_page.text)
    # page table call
    if count == 1:
        page_df = page_table(driver)
        #print(page_df.head())
        old_df = page_df
        count = 0
    else:
        page_df = page_table(driver)
        #print(page_df.head())
        old_df = df_appender(old_df, page_df)
    ##
    next_page.click()
    time.sleep(8)
    return val


def stock_table(url, chrome_path=PATH_TO_CHROMEDRIVER):
    # URL from where the tables will be scraped
    try:
        global old_df, count

        #URL = 'https://chartink.com/screener/strong-move-range-break-out-with-volume-and-obv-75min'
        #URL = 'https://chartink.com/screener/strong-stocks'
        URL = url
        #URL = input()
        # define driver as firefox webdriver
        #driver = webdriver.Safari()

        options = Options()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(executable_path=PATH_TO_CHROMEDRIVER, options= options)

        #driver.maximize_window()
        time.sleep(2)
        # loads the page in firefox
        driver.get(URL)

        while True:
            next_val = paginator(driver)
            #print(next_val)
            if next_val == 'paginate_button next disabled':
                #print('breaking...')
                break

        print('-------------------------------------------------')
        old_df = old_df.reset_index(drop=True)
        print(old_df)
        print('--------------------------------------')

        try:
            create_dir(DATA_DIR)
            old_df.to_csv(DATA_DIR+str('master.csv'), mode='a', index=False, header=False)
            ct = dt.now().strftime("%d-%m-%Y--%H-%M-%S")
            old_df.to_csv(DATA_DIR + f'{ct}.csv', index=False)
            # Column names

            driver.close()
        # Use try except block to extract the tables from html and to catch the exception gracefully if the table doesnot exist
        except Exception as ex:
            driver.close()
            sys.exit(0)

    except Exception as ex:
        # exit program
        sys.exit(0)
