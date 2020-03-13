"""module for Covid19Processing class"""
import logging
import math
import os
import sys
import requests
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
import pandas_bokeh
import copy


class Covid19Processing:
    """Downloads and process time series data from
    https://github.com/CSSEGISandData/COVID-19/
    """

    def __init__(self, filename, out_dir, full_url):

        self.filename = filename
        self.out_dir = out_dir
        self.full_url = full_url
        print(filename)
        logging.debug(f'Covid19Processing working on {filename}')

    def create_out_dir(self):
        """creates a new output directory out_dir
        This will be used for all files to be written"""

        logging.debug(f'create_out_dir called'
                      f'Output directory to be created:'
                      f' {self.out_dir}')

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
                    logging.debug(f'Creation of directory has failed '
                                  f'at: {path}')
                else:
                    logging.debug(f'Successfully created the '
                                  f'directory path at:{path}')
        return self.out_dir, list_outs

    def download_from_github(self):
        """downloads the datasets from the COVID19 github repo
        into instance variable storage
        """
        logging.debug('download_from_github called')
        self.response = requests.get(f'{self.full_url}{self.filename}')
        status_code = self.response.status_code
        if status_code == 200:
            logging.debug('Success response gave status code 200')
            with open(f'{self.out_dir}/downloaded/{self.filename}',
                      'wb') as csv_written:
                csv_written.write(self.response.content)
        else:
            logging.debug(f'Error in requests download'
                          f'status_code={status_code}')
            sys.exit()

        return self.response

    def process_data(self):
        """processes the stored data into a form for CSV files"""
        logging.debug('process_data called')

        pd_time_series = pd.read_csv(f'{self.out_dir}/downloaded/'
                                     f'{self.filename}')
        pd_time_series = pd_time_series.drop('Lat', axis=1)
        pd_time_series = pd_time_series.drop('Long', axis=1)
        no_of_dates = len(pd_time_series.columns) - 2
        dateindex = pd.date_range(start='1-22-2020', periods=no_of_dates,
                                  freq='D').strftime('%d-%m')

        new_cols = ['Province/State', 'Country/Region']
        for index in dateindex:
            new_cols.append(index)
        pd_time_series.columns = new_cols

        pd_time_series = pd_time_series.drop('Province/State', axis=1)
        pd_edit_series = pd_time_series.set_index('Country/Region')

        pd_edit_series = pd_edit_series.T

        # Future addition
        # pd_edit_series.loc[:, 'Daily Total'] =
        # pd_edit_series.sum(numeric_only=True, axis=1)

        return pd_edit_series

    def write_csv_files(self, pd_edit_series):
        """writes CSV files to out_dir"""
        logging.debug(f'write_csv_files called. File saved to:'
                      f'{self.out_dir}/edited_csv/{self.filename}')

        pd_edit_series.to_csv(f'{self.out_dir}/edited_csv/'
                              f'edited_{self.filename}',
                              encoding='utf-8')

    @staticmethod
    def data(pd_edit_series):
        """
        A function where the imported data will be further
        edited in a more extensive manner.
        """
        country_dict = {
            'europe': ['United Kingdom', 'France', 'Spain', 'Belgium',
                       'Finland', 'Sweden', 'Germany', 'Croatia',
                       'Switzerland', 'Austria', 'Greece', 'Hungary',
                       'Slovenia', 'Poland', 'Bosnia and Herzegovina',
                       'Denmark', 'Liechtenstein', 'Ukraine',
                       'North Macedonia', 'Latvia', 'Andorra',
                       'Norway', 'Portugal', 'Romania', 'Estonia',
                       'Netherlands', 'San Marino', 'Belarus',
                       'Iceland', 'Lithuania', 'Ireland', 'Luxembourg',
                       'Monaco', 'Czechia', 'Slovakia', 'Holy See',
                       'Serbia', 'Malta', 'Bulgaria', 'Albania',
                       'Cyprus', 'Moldova', 'Andorra', 'Armenia',
                       'Austria', 'Cyprus', 'Estonia', 'Georgia',
                       'Gibraltar', 'Greenland', 'Croatia',
                       'Israel', 'Iceland', 'Luxembourg',
                       'Latvia', 'Monaco', 'Portugal', 'Romania',
                       'Svalbard and Jan Mayen', 'Slovakia',
                       'Turkey', 'Serbia', 'Montenegro',
                       'Aland Islands', 'Guernsey',
                       'Island of Man', 'Jersey'],

            'asia': ['Thailand', 'Japan', 'Singapore', 'Mongolia',
                     'Nepal', 'Malaysia', 'Sri Lanka', 'Philippines',
                     'India', 'Cambodia', 'Pakistan', 'Georgia',
                     'Indonesia', 'United Arab Emirates', 'Lebanon',
                     'Iraq', 'Oman', 'Afghanistan', 'Bahrain',
                     'Kuwait', 'Israel', 'Qatar', 'Saudi Arabia',
                     'Jordan', 'Azerbaijan', 'Bhutan', 'Maldives',
                     'Bangladesh', 'Brunei', 'Korea, South', 'Vietnam',
                     'Russia', 'Iran', 'Reunion', 'Taiwan*', 'Yemen',
                     'American Samoa', 'Brunei Darussalam',
                     'Guam', 'Hong Kong',
                     'Heard Island and McDonald Islands',
                     'British Indian Ocean Territory',
                     'Kyrgystan', 'Kiribati', 'Korea, North',
                     'Kazakhstan', 'Sri Lanka', 'Marshall Islands',
                     'Lao People\'s Democratic Republic',
                     'Myanmar', 'Mongolia', 'Macau', 'Macao SAR',
                     'North Mariana Islands', 'Maldives',
                     'Malaysia', 'Papua New Guinea', 'Palau',
                     'Singapore', 'Syrian Arab Republic',
                     'Tajikistan', 'Turkmenistan', 'Timor-Leste',
                     'United States Minor Outlying Islands',
                     'Uzbekistan', 'Tunisia', 'Somalia',
                     'Palestinian Territory', 'Mauritania', 'Morocco',
                     'Comoros', 'Algeria', 'Djibouti', 'Bahrain'],

            'africa': ['Egypt', 'Algeria', 'Nigeria',
                       'Morocco', 'Senegal', 'Tunisia',
                       'South Africa', 'Togo', 'Cameroon',
                       'Burkina Faso', 'Cote d\'Ivoire',
                       'Congo (Kinshasa)'],

            'americas': ['Brazil', 'Mexico', 'Ecuador',
                         'Dominican Republic', 'Argentina',
                         'Chile', 'Peru', 'Netherlands Antilles',
                         'Costa Rica', 'Colombia', 'French Guiana',
                         'Martinique', 'Paraguay', 'Panama',
                         'Canada', 'US', 'Jamaica', 'Honduras',
                         'Bolivia', 'Antigua and Barbuda', 'Anguilla',
                         'Argentina', 'Aruba', 'Barbados',
                         'Bouvet Island', 'Belize', 'Cuba', 'Dominica',
                         'Equador', 'Falkland Islands', 'Malvinas',
                         'Grenada', 'Guadeloupe', 'Guyana',
                         'South Georgia and the South Sandwich '
                         'Islands', 'US',
                         'Guatemala', 'Haiti', 'Saint Kitts and Nevis',
                         'Cayman Islands', 'Saint Lucia', 'Montserrat',
                         'Mexico', 'Nicaragua', 'Puerto Rico',
                         'Paraguay', 'Suriname', 'El Salvador',
                         'Turks and Caicos Islands',
                         'Trinidad and Tobago', 'Uruguay',
                         'Saint Vincent and the Grenadines',
                         'Venezuela', 'Virgin Islands (British)',
                         'Virgin Islands (US)', 'Saint Martin',
                         'Saint Berthelemy', 'Bermuda',
                         'Saint Pierre and Miquelon', 'Cuba', 'Guyana'],

            'oceania': ['Australia', 'New Zealand', 'New Caledonia',
                        'Norfolk Island', 'Nauru', 'Niue',
                        'Micronesia (federated States of)', 'Fiji',
                        'Cook Islands', 'Christmas Island',
                        'Cocos (Keeling) Islands', 'French Polynesia',
                        'Pitcairn Islands', 'Solomon Islands',
                        'French Southern Territories',
                        'American Samoa', 'Tokelau', 'Tonga', 'Tuvalu',
                        'Vanuatu', 'Wallis and Futuna', 'Samoa']}

        europe = []
        asia = []
        oceania = []
        americas = []
        africa = []
        uk = []
        italy = []
        china = []
        others = []
        ship = []
        all_lists = [europe, asia, oceania, americas, africa, uk,
                     italy, china, ship]
        for_total = [europe, asia, oceania, americas, africa, china,
                     others, ship]

        for region, countries in country_dict.items():
            for column in pd_edit_series:
                if column in countries:
                    if region == 'europe':
                        if column not in europe:
                            europe.append(column)
                            if column == 'United Kingdom' or 'UK':
                                if column not in uk:
                                    uk.append(column)
                    elif region == 'asia':
                        if column not in asia:
                            asia.append(column)
                    elif region == 'africa':
                        if column not in africa:
                            africa.append(column)
                    elif region == 'americas':
                        if column not in americas:
                            americas.append(column)
                    elif region == 'oceania':
                        if column not in oceania:
                            oceania.append(column)
                    elif column == 'Diamond Princess' or 'Cruise Ship':
                        if column not in ship:
                            ship.append(column)
                            print(ship)
                else:
                    if column == 'Italy':
                        if column not in italy:
                            italy.append(column)

                    elif column == 'China' or 'Mainland China':
                        if column not in china:
                            china.append(column)

                    else:
                        others.append(column)
        sys.exit()
        # -----------------------------------------------------------
        # Segment of code it to catch any straggler countries not
        # accounted for in the country_dict
        remove_list = []
        for list in all_lists:
            for countries in list:
                if countries in others:
                    if countries not in remove_list:
                        remove_list.append(countries)

        others_final = [item for item in others
                        if item not in remove_list]
        
        if others_final > 0:
            print(others_final)
            print('Exitting due to unaccounted countries')
            sys.exit()
        # -----------------------------------------------------------

        diamond_csv = pd_edit_series[ship].copy()
        main_china_csv = pd_edit_series[china].copy()
        europe_csv = pd_edit_series[europe].copy()
        americas_csv = pd_edit_series[americas].copy()
        asia_csv = pd_edit_series[asia].copy()
        africa_csv = pd_edit_series[africa].copy()
        uk_csv = pd_edit_series[uk].copy()
        italy_csv = pd_edit_series[italy].copy()
        oceania_csv = pd_edit_series[oceania].copy()

        csv_list = {'europe': europe_csv, 'america': americas_csv,
                    'asia': asia_csv, 'main_china': main_china_csv,
                    'UK': uk_csv, 'diamond': diamond_csv,
                    'italy': italy_csv, 'oceania': oceania_csv,
                    'africa': africa_csv}

        pd_edit_series['Mainland_China_Total'] = \
            pd_edit_series[china].sum(axis=1)

        pd_edit_series['Oceania Total'] = \
            pd_edit_series[oceania].sum(axis=1)

        pd_edit_series['Europe_Total'] = \
            pd_edit_series[europe + ['Italy']].sum(axis=1)

        pd_edit_series['Diamond_Princess'] = \
            pd_edit_series[ship]

        pd_edit_series['UK_Total'] = \
            pd_edit_series[uk].sum(axis=1)

        pd_edit_series['Asian_Total'] = \
            pd_edit_series[asia].sum(axis=1)

        pd_edit_series['Americas_Total'] = \
            pd_edit_series[americas].sum(axis=1)

        pd_edit_series['African_Total'] = \
            pd_edit_series[africa].sum(axis=1)

        # As China is being kept separate
        pd_edit_series = pd_edit_series.drop('China', axis=1)
        pd_edit_series = pd_edit_series.drop('Cruise Ship', axis=1)

        for place in asia:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in europe:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in americas:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in africa:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
        for place in oceania:
            pd_edit_series = pd_edit_series.drop(place, axis=1)
            print(ship)
        print(pd_edit_series)
        return csv_list, pd_edit_series

    def write_new_csv(self, pd_edit_series, csv_list):
        """
        Saving The new edited csvs and total csv
        """
        logging.debug(f'write_new_csvs called. File saved to:'
                      f'{self.out_dir}edited_csv/')

        pd_edit_series.to_csv(f'{self.out_dir}edited_csv/'
                              f'edited_location_totals',
                              encoding='utf-8')

        for country, csv in csv_list.items():
            csv.to_csv(f'{self.out_dir}edited_csv/edited_{country}')

    @staticmethod
    def round_up(number, decimals=0):
        """
        A function to aid in the production of more
        flexible y axis integers
        """
        multiplier = 10 ** decimals
        return math.ceil(number * multiplier) / multiplier

    def plot_data(self, data):
        """
        A function to plot the graphs with an increased 'ceiling' 
        """
        title = self.filename.split('-')
        final_titles = title[2].split('.')
        self.final_title_sub = final_titles[0].lower()
        print(self.final_title_sub)

        for column in data.columns:
            subset = data.loc[:, data.columns != str(column)]

            data['Rest of the World'] = subset.sum(axis=1)
            x_axis = data.index.values

            fig, axes = plt.subplots()
            axes.plot(x_axis, data[column], marker='o',
                      label=column)
            axes.plot(x_axis, data['Rest of the World'], marker='s',
                      label='Rest of the World')

            every_nth = 4
            for number, label in enumerate(axes.xaxis.get_ticklabels()):
                if number % every_nth != 0:
                    label.set_visible(False)
            axes.set(xlabel='Date', ylabel='Cases',
                     title=f'Covid-19 {self.final_title_sub} cases for '
                           f'{column} - data from John Hopkins CSSE')
            axes.grid()
            axes.legend()

            # Setting the y axis
            data_max = data.max(axis=1)
            max_number = data_max[-1]
            rounded_max = self.round_up(max_number, -3)
            rounded_max += 2000
            axes.set_ylim([0, rounded_max])

            # Adds Labels to annotate the last data point for each plot
            y_axis1 = data[column][-1]
            y_axis2 = data['Rest of the World'][-1]

            plt.annotate(y_axis1, (x_axis[-1], y_axis1 + 500),
                         bbox=dict(facecolor='blue', alpha=0.5),
                         fontsize=12)
            plt.annotate(y_axis2, (x_axis[-1], y_axis2 + 500),
                         bbox=dict(facecolor='red', alpha=0.5),
                         fontsize=12)

            # Required in order to stop the column from summing
            # the total of each run through the loop
            # otherwise this leads to Rest of World values in the
            # millions
            data = data.drop('Rest of the World', axis=1)

            self.dir_name = f'{self.out_dir}graphics/' \
                            f'{x_axis[-1]}-2020-' \
                            f'{self.final_title_sub}_for_{column}.png'
            self.web_name = f'{self.out_dir}graphics/' \
                            f'{self.final_title_sub}_for_{column}.png'
            fig.savefig(self.dir_name, transparent=False, dpi=300,
                        bbox_inches="tight")
            fig.savefig(self.web_name, transparent=False, dpi=300,
                        bbox_inches="tight")

            if os.path.exists(self.dir_name):
                logging.debug(f'File saved at: {self.dir_name}')
                logging.debug(f'File saved at: {self.web_name}')
                print(f'Files saved at:\n'
                      f'{self.dir_name}\n'
                      f'{self.web_name}')
            else:
                logging.debug('Failed to save')
            logging.debug(os.getcwd())
        plt.close()
        return data

    def bokehplot(self, data):
        """
        A function to produce advanced interactive plots with the use
        of bokeh
        """
        subset = data.loc[:, data.columns]
        data['Total_Cases'] = subset.sum(axis=1)

        plotted = data.plot_bokeh(title=f'Global Data for Covid-19 '
                                        f'{self.final_title_sub}',
                                  figsize=(1000, 750),
                                  legend='top_left',
                                  xlabel='Dates - '
                                         'Formatted (Day/Month)',
                                  ylabel='Number of Cases',
                                  disable_scientific_axes='y',
                                  return_html=True,
                                  show_figure=False)

        save_to = f'{self.out_dir}graphics/interactive_plot_for_' \
                  f'{self.final_title_sub}.html'
        logging.debug(f'Interactive plot saved to:\n{save_to}')

        with open(save_to, 'w') as int_plot:
            int_plot.write(plotted)
