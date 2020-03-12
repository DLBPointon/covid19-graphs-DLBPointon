"""
------------------------------------------------------------------------------
-- Covid19_Processing Scripts - tools to download and process COVID-19 data --
------------------------------------------------------------------------------
------------------------------- By S.I.D 1836811 -----------------------------
------------------------------------------------------------------------------
This script is designed to be a 'one argument and do everything' kind of
script.

Method:
Simply calling the package and clarifying the output directory should allow
for the downloading of data from the John Hopkins repo.

The subsequent parsing of said data.

The downloading of the website repo.

Updating the website repo with the graphics produced from the covid package.

Re-uploading the 

"""
import argparse
import logging
import requests
import sys
import os
from covid19_graphs.covid19_processing import Covid19Processing


def parse_command_line_args(test_override=None):
    """Parse options returning the args namespace

    Sets up the command line using argparse including the help message.
    Here a single sequence string is required for output directory is
    required.

    test_override is an optional list of arguments (this is for testing).

    returns the args namespace that can be used for control
    """
    parser = argparse.ArgumentParser(description=__doc__)

    help_ = 'directory for output files '
    parser.add_argument('out_dir',
                        metavar='OUT_DIR',
                        help=help_)

    help_ = 'turn on debug message logging output'
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help=help_)

    if test_override is not None:
        args = parser.parse_args(test_override)
    else:
        args = parser.parse_args()
    return args


def site_update_helper():
    """
    A function to add functionality to allow website usage
    """
    if os.path.exists('/home/runner/work'):
        print('Working on GitHub')
        os.popen('cp -rf graphics /home/runner/work')
    else:
        print('Working on Local machine')

        os.chdir('../')
        print(os.getcwd())
        
        repo = 'https://github.com/DLBPointon/dlbpointon.github.io.git'

        if os.path.exists('dlbpointon.github.io'):
            print('Website repo already downloaded')
        else:
            os.popen(f'git clone {repo}')
            print('Website downloading')
        os.popen('cp -rf covid19-graphs-DLBPointon/graphics dlbpointon.github.io/')
        os.popen('python dlbpointon.github.io/website_updater.py')


def main():
    """ main function invoked by covid19 script"""
    args = parse_command_line_args()
    # turn on debug level logging if user specifies --debug
    if args.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='debug %(message)s')
    print(__doc__)
    out_dir = args.out_dir
    logging.debug(f'args namespace: {args}')
    logging.debug(f'will output to directory: {out_dir}')

    file_names = ['time_series_19-covid-Confirmed.csv',
                  'time_series_19-covid-Deaths.csv',
                  'time_series_19-covid-Recovered.csv']

    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
    folder = 'csse_covid_19_data/csse_covid_19_time_series/'
    full_url = f'{url}{folder}'

    for file in file_names:
        c_process = Covid19Processing(file, out_dir, full_url)
        c_process.create_out_dir()
        c_process.download_from_github()
        pd_edit_series = c_process.process_data()
        c_process.write_csv_files(pd_edit_series)
        csv_list, data = c_process.data(pd_edit_series)
        c_process.write_new_csv(pd_edit_series, csv_list)
        c_process.plot_data(data)

    # site_update_helper()


if __name__ == '__main__':
    main()
