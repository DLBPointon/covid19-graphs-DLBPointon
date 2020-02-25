"""module for Covid19Processing class"""
import logging


class Covid19Processing():
    """Downloads and process time series data from
    https://github.com/CSSEGISandData/COVID-19/
    """

    def __init__(self):
        logging.debug('Covid19Processing __init__ to be written')  # TODO
        # TODO add instance variables to store the data here
        # TODO decide on how we are going to store

    def download_from_github(self):
        """downloads the datasets from the COVID19 github repo
        into instance variable storage
        """
        logging.debug('download_from_github to be written')  # TODO
        # TODO use requests to download the datasets

    def process_data(self):
        """processes the stored data into a form for CSV files"""
        logging.debug('process_data to be written')  # TODO

    def create_out_dir(self, out_dir):
        """creates a new output directory out_dir

        This will be used for all files to be written"""
        # TODO decide on what happens if the directory already exists!
        logging.debug(f'create_out_dir to be written, {out_dir}')  # TODO

    def write_csv_files(self, out_dir):
        """writes CSV files to out_dir"""
        logging.debug(f'write_csv_files to be written, {out_dir}')  # TODO
