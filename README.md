
![PyLint and PyCodeStyle Compliance](https://github.com/ARU-Bioinf-ISE/covid19-graphs-DLBPointon/workflows/Python%20application/badge.svg?branch=master)
![automated_script_runner](https://github.com/ARU-Bioinf-ISE/covid19-graphs-DLBPointon/workflows/automated_script_runner/badge.svg)

# A tool to download and plot Covid-19 disease outbreak data

Please see [README_instructions.md](README_instructions.md)


## Installing the `covid19_graphs` package (for developers)

To install the `covid19_graphs` package first git clone this repo
then 
```
cd REPO_DIR
pip install -e . 
```
To test your installation run the `covid19_graphs` command line script.
```
covid19_graphs -h
```
If script is run manually please ensure the OUT_DIR ends with '/' for example
'./'.

You should get an output like
```
$ covid19_graphs -h
------------------------------------------------------------------------------
-- Covid19_Processing Scripts - tools to download and process COVID-19 data --
------------------------------------------------------------------------------
------------------------------- By S.I.D 1836811 -----------------------------
------------------------------------------------------------------------------
This script is designed to be a 'one argument and do everything' kind of
script.
------------------------------------------------------------------------------
Method: Simply calling the package and clarifying the output directory should
allow for the downloading of data from the John Hopkins repo. The subsequent
parsing of said data. This data is graphed by the modules matplotlib and
pandas-bokeh (a back-end plug in for bokeh.io. This data (downloaded, edited
and graphed) are then saved to their representative folders. The graphics
folder will be hosted in the ./docs where a github pages is built upon commit
to the repo.
------------------------------------------------------------------------------
The planned automation for this script will enable it to be run via a github
action workflow and be presented on the github page found at the following
link: https://aru-bioinf-ise.github.io/covid19-graphs-DLBPointon/
------------------------------------------------------------------------------

positional arguments:
  OUT_DIR      directory for output files

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  turn on debug message logging output

```
This script however does not require being run manually as a number
 of workflows have been written to ensure that this project is run at
 12:00pm daily and then updates the repo automatically and with out 
 human interference.
 
Once updated via the workflow, the github pages will be rebuilt allowing
 everything to be shows on: [This Site](https://aru-bioinf-ise.github.io/covid19-graphs-DLBPointon/).

Graphs for the visual representation of data will be present in three forms.

Linear graphs:

![Confirmed Africa](docs/graphics/confirmed_for_African_Total.png)

Logarithmic graphs:

![Log Africa](docs/graphics/log_confirmed_for_African_Total.png)

And Interactive graphs (due to their html nature they cannot be added directly 
to a static page:

[Found here](docs/graphics/interactive_plot_for_confirmed.html).

The csvs that these graphs are based upon can be found on here:

[CSV Page](https://aru-bioinf-ise.github.io/covid19-graphs-DLBPointon/csv_page.html)