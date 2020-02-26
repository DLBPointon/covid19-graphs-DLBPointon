"""module for Covid19Processing class"""
import logging
import requests
import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_names = ['time_series_19-covid-Confirmed.csv',
              'time_series_19-covid-Deaths.csv',
              'time_series_19-covid-Recovered.csv']
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
folder = 'csse_covid_19_data/csse_covid_19_time_series/'
full_url = f'{url}{folder}'
out_dir = './output'


class Covid19Processing:
    """Downloads and process time series data from
    https://github.com/CSSEGISandData/COVID-19/
    """

    def __init__(self, filename, out_dir, full_url):
        self.filename = filename
        self.out_dir = out_dir
        self.full_url = full_url
        print(filename)
        logging.debug('Covid19Processing __init__ to be written')  # TODO
        # TODO add instance variables to store the data here
        # TODO decide on how we are going to store

    def create_out_dir(self):
        """creates a new output directory out_dir
        This will be used for all files to be written"""

        logging.debug(f'create_out_dir called'
                      f'Output directory to be created: {self.out_dir}')

        access_rights = 0o755

        if os.path.exists(self.out_dir):
            logging.debug(f'Path: {self.out_dir} :already exists')
        else:
            try:
                os.makedirs(self.out_dir, access_rights)
            except OSError:
                logging.debug(f'Creation of directory has failed at:'
                              f'{self.out_dir}')
            else:
                logging.debug(f'''Successfully created the directory path at:
                                    {self.out_dir}''')
        return self.out_dir

    def download_from_github(self):
        """downloads the datasets from the COVID19 github repo
        into instance variable storage
        """
        logging.debug('download_from_github called')

        self.response = requests.get(f'{self.full_url}{self.filename}')
        status_code = self.response.status_code
        if status_code == 200:
            print('Success response gave status code 200')
            with open(f'{self.out_dir}/downloaded_{self.filename}',
                      'wb') as csv_written:
                csv_written.write(self.response.content)
        else:
            print(f'Error in requests download status_code={status_code}')
            sys.exit()

        return self.response

    def process_data(self):
        """processes the stored data into a form for CSV files"""
        logging.debug('process_data called')

        self.data_csv = pd.read_csv(f'{self.out_dir}/downloaded_'
                                    f'{self.filename}')
        return self.data_csv

    def write_csv_files(self):
        """writes CSV files to out_dir"""
        logging.debug(f'write_csv_files called. File saved to:'
                      f'{self.out_dir}')