import os


if os.name == 'nt':
    DATA_DIR = r'.\\data\\'
    PATH_TO_CHROMEDRIVER = r'.\\chromedriver'

else:
    DATA_DIR = './data/'
    PATH_TO_CHROMEDRIVER = './chromedriver'


