"""module for Covid19Processing class"""
import logging
import requests
import sys
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import string
import math

file_names = ['time_series_19-covid-Confirmed.csv',
              'time_series_19-covid-Deaths.csv',
              'time_series_19-covid-Recovered.csv']
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
folder = 'csse_covid_19_data/csse_covid_19_time_series/'
full_url = f'{url}{folder}'


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
        list_outs = ['downloaded', 'edited_csv', 'graphics']
        for dir in list_outs:
            path = self.out_dir + dir
            if os.path.exists(path):
                logging.debug(f'Path: {path} :already exists')
            else:
                try:
                    os.makedirs(path, access_rights)
                except OSError:
                    logging.debug(f'Creation of directory has failed at:'
                                  f'{path}')
                else:
                    logging.debug(f'''Successfully created the directory path at:
                                        {path}''')
        return self.out_dir, list_outs

    def download_from_github(self):
        """downloads the datasets from the COVID19 github repo
        into instance variable storage
        """
        logging.debug('download_from_github called')

        self.response = requests.get(f'{self.full_url}{self.filename}')
        status_code = self.response.status_code
        if status_code == 200:
            print('Success response gave status code 200')
            with open(f'{self.out_dir}/downloaded/{self.filename}',
                      'wb') as csv_written:
                csv_written.write(self.response.content)
        else:
            print(f'Error in requests download status_code={status_code}')
            sys.exit()

        return self.response

    def process_data(self):
        """processes the stored data into a form for CSV files"""
        logging.debug('process_data called')

        pd_time_series = pd.read_csv(f'{self.out_dir}/downloaded/{self.filename}')
        pd_time_series = pd_time_series.drop('Lat', axis=1)
        pd_time_series = pd_time_series.drop('Long', axis=1)
        no_of_dates = len(pd_time_series.columns) - 2
        dateindex = pd.date_range(start='1-22-2020', periods=no_of_dates, freq='D').strftime('%d-%m')

        new_cols = ['Province/State', 'Country/Region']
        for index in dateindex:
            new_cols.append(index)
        pd_time_series.columns = new_cols

        pd_time_series = pd_time_series.drop('Province/State', axis=1)
        pd_edit_series = pd_time_series.set_index('Country/Region')
        # pd_edit_series = pd_time_series

        pd_edit_series = pd_edit_series.T
        # pd_edit_series.loc[:, 'Daily Total'] = pd_edit_series.sum(numeric_only=True, axis=1)

        return pd_edit_series

    def write_csv_files(self, pd_edit_series):
        """writes CSV files to out_dir"""
        logging.debug(f'write_csv_files called. File saved to:'
                      f'{self.out_dir}/edited_csv/{self.filename}')
        pd_edit_series.to_csv(f'{self.out_dir}/edited_csv/edited_{self.filename}', encoding='utf-8')

    def data(self, pd_edit_series):
        """
        A function where the imported data will be further edited in a more extensive manner.
        """
        europe = ['France', 'Spain', 'Italy', 'Belgium', 'Finland',
                  'Sweden', 'Germany', 'Croatia', 'Switzerland', 'Austria',
                  'Greece', 'Hungary', 'Slovenia', 'Gibraltar', 'Poland',
                  'Bosnia and Herzegovina', 'Faroe Islands', 'Liechtenstein',
                  'Ukraine', 'North Macedonia', 'Latvia', 'Andorra', 'Norway',
                  'Portugal', 'Romania', 'Denmark', 'Estonia', 'Netherlands',
                  'San Marino', 'Belarus', 'Iceland', 'Lithuania', 'Ireland',
                  'Luxembourg', 'Monaco', 'Czech Republic', 'Vatican City',
                  'Slovakia', 'Serbia', 'Malta']

        asia = ['Thailand', 'Japan',
                'South Korea', 'Taiwan', 'Macau',
                'Hong Kong', 'Singapore', 'Vietnam',
                'Nepal', 'Malaysia', 'Sri Lanka',
                'Philippines', 'India',
                'Cambodia', 'Russia', 'Pakistan',
                'Georgia', 'Indonesia',
                'United Arab Emirates', 'Iran', 'Lebanon',
                'Iraq', 'Oman', 'Afghanistan',
                'Bahrain', 'Kuwait', 'Israel',
                'Qatar', 'Palestine', 'Saudi Arabia',
                'Jordan', 'Azerbaijan', 'Armenia',
                'Bhutan']

        africa = ['Egypt', 'Algeria', 'Nigeria',
                  'Morocco', 'Senegal', 'Tunisia',
                  'South Africa', 'Togo', 'Cameroon']

        americas = ['Brazil', 'Mexico', 'Ecuador',
                    'Dominican Republic', 'Argentina',
                    'Chile', 'Saint Barthelemy', 'Peru',
                    'Costa Rica', 'Colombia', 'French Guiana',
                    'Martinique']

        europe_csv = pd_edit_series[europe + ['UK']].copy()
        americas_csv = pd_edit_series[americas].copy()
        asia_csv = pd_edit_series[asia].copy()
        main_china_csv = pd_edit_series.loc[:, 'Mainland China'].copy()
        uk_csv = pd_edit_series.loc[:, 'UK'].copy()
        diamond_csv = pd_edit_series.loc[:, 'Others'].copy()
        csv_list = {'europe': europe_csv, 'america': americas_csv, 'asia': asia_csv,
                    'main_china': main_china_csv, 'UK': uk_csv, 'diamond': diamond_csv}

        pd_edit_series['Mainland_China_Total'] = pd_edit_series.loc[:, 'Mainland China'].sum(axis=1)

        pd_edit_series['US_Total'] = pd_edit_series.loc[:, 'US'].sum(axis=1)

        pd_edit_series['Canada_Total'] = pd_edit_series.loc[:, 'Canada'].sum(axis=1)

        pd_edit_series['Australia_Total'] = pd_edit_series[['Australia', 'New Zealand']].sum(axis=1)

        pd_edit_series['Europe_Total'] = pd_edit_series[europe + ['UK']].sum(axis=1)

        pd_edit_series['Diamond_Princess'] = pd_edit_series[['Others']]

        pd_edit_series['UK_Total'] = pd_edit_series[['UK']]

        pd_edit_series['Asian_Total'] = pd_edit_series[asia].sum(axis=1)

        pd_edit_series['Americas_Total'] = pd_edit_series[americas].sum(axis=1)

        pd_edit_series['African_Total'] = pd_edit_series[africa].sum(axis=1)

        pd_edit_series = pd_edit_series.drop('Mainland China', axis=1)
        pd_edit_series = pd_edit_series.drop('US', axis=1)
        pd_edit_series = pd_edit_series.drop('Canada', axis=1)
        pd_edit_series = pd_edit_series.drop('Australia', axis=1)
        pd_edit_series = pd_edit_series.drop('New Zealand', axis=1)

        for place in asia:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in europe:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in americas:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in africa:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        pd_edit_series = pd_edit_series.drop('UK', axis=1)
        pd_edit_series = pd_edit_series.drop('Others', axis=1)

        return csv_list, pd_edit_series

    def write_new_csv(self, pd_edit_series, csv_list):
        """
        Saving The new edited csvs and total csv
        """
        logging.debug(f'write_new_csvs called. File saved to:'
                      f'{self.out_dir}edited_csv/')
        pd_edit_series.to_csv(f'{self.out_dir}edited_csv/edited_location_totals', encoding='utf-8')

        for country, csv in csv_list.items():
            csv.to_csv(f'{self.out_dir}edited_csv/edited_{country}')

    def round_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

    def plot_data(self, data):
        """
        A function to plot the graphs from the imported data
        """
        title = self.filename.split('-')
        final_title = title[2].split('.')

        data = data.drop('UK_Total', axis=1)
        data = data.drop('US_Total', axis=1)
        data = data.drop('Canada_Total', axis=1)

        for column in data.columns:
            data['Rest of the World'] = data.loc[:, data.columns != str(column)].sum(axis=1)
            x = data.index.values
            fig, ax = plt.subplots()
            ax.plot(x, data[column], marker='o', label=column)
            ax.plot(x, data['Rest of the World'], marker='s', label='Rest of the World')

            every_nth = 4
            for number, label in enumerate(ax.xaxis.get_ticklabels()):
                if number % every_nth != 0:
                    label.set_visible(False)
            ax.set(xlabel='Date', ylabel='Cases',
                   title=f'Covid-19 {final_title[0]} cases for {column} - data from John Hopkins CSSE')
            ax.grid()
            ax.legend()

            # Setting the y axis
            data_max = data.max(axis=1)
            max_number = data_max[-1]
            rounded_max = self.round_up(max_number, -3)
            rounded_max += 2000
            ax.set_ylim([0, rounded_max])

            y1 = data[column][-1]
            y2 = data['Rest of the World'][-1]

            # Adds Labels to annotate the last data point for each plot
            plt.annotate(y1, (x[-1], y1+500), bbox=dict(facecolor='blue', alpha=0.5), fontsize = 12)
            plt.annotate(y2, (x[-1], y2+500), bbox=dict(facecolor='red', alpha=0.5), fontsize = 12)

            # Required in order to stop the column from summing the total of each run through the loop
            data = data.drop('Rest of the World', axis=1)
            dir_name = f'{self.out_dir}graphics/{final_title[0]}_for_{column}.png'
            fig.savefig(dir_name, transparent=False, dpi=300, bbox_inches="tight")
            if os.path.exists(dir_name):
                print(f'File saved at:'
                      f'{dir_name}')
            else:
                print('Failed to save')

        plt.close()
