
![PyLint and PyCodeStyle Compliance](https://github.com/ARU-Bioinf-ISE/covid19-graphs-DLBPointon/workflows/Python%20application/badge.svg?branch=master)
![automated_script_runner](https://github.com/ARU-Bioinf-ISE/covid19-graphs-DLBPointon/workflows/automated_script_runner/badge.svg)

# A tool to download and plot Covid-19 disease outbreak data

## NO LONGER MAINTAINED -
## SOFTWARE DEVELOPMENT COURSEWORK 2020

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

---
#### Graphs and CSV files
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

---
#### Testing
Rather than using PyTest the developer has chosen to use Manual Testing.

Each function was tested individually in order to gage to the end result.
This was achieved early on by testing the functions as they were built,
0.01and later on by introducing sys.exit() at certain locations in order to neatly break the script at key points.
This includes in between functions and when debugging.

#### covid19_processing.py testing

create_out_dir:
Tested by giving the out_dir arg and then locating the produced folder structure.

download_from_github:
Tested by allowing the creation of folders and allowing the downloading of the files from github.
These will then be found in the 'downloaded' folder.

process_data:
Testing was performed by allowing the previous functions and added print statements
before and after each modification, these include the removal of:
- long/lat data 
- Province data
- Transposing the data so that the data in the requested format (dates down the left side and countries across the top).

write_csv_files:
Testing this script was performed by allowing the previous functions to run followed by this one.
This would result in an edited_csv being produced in the edited_CSV file produced by the create_out_dir function.

data:
Testing this function requires the running of all previous functions as well as frequent use of print() after every
modification of the data set. This includes the printing of:
- All lists at frequent intervals.
- All sub-sets of the original data set.
- The main data table after every modification - dropping/additions of columns.

write_new_csv:
Created as use of the previous write_csv files function would not have been suitable.
Testing this function required the product of the previous functions and writes the produced subsets to the respective
folder produced by the create_out_dir function.

round_up:
This function was produced in order to allow for better production of graphs (specifically y-axis production).
This was produced and tested after the production of the plot_data function.

plot_data:
This function contains all the logic for producing the static matplotlib graphs used throughout this production.
This was tested repeatedly via printing the columns to be used for each graph and then the cross-referencing of various 
data points with the original data. Although this was much more time consuming than automated testing, 
it is felt that it was much more thorough.
Once it came to adding the annotations this data value could then be used as an invaluable test for whether the
logic is being adhered to. Values too high indicated that some columns were being repeatedly summed. This was the case
when originally testing this function as the Rest of the world column would be summed for each run through the previous
function leading the misleading value to begin as the correct value for the first graph and then grow exponentially until the last graph.
This was subsequently fixed by removing the rest of the world column at the end of the production of graph.

Once testing of the data set was completed, testing of the labelling and saving segments where completed by looking for the produced file
in the representative folder produced by the create_out_dirs function.

bokehplot:
Testing for this function was completed by using a basic framework using the online documentation for the pandas-bokeh backend module 
(an add on for the original bokeh.io module which does not agree with some of the data types used in the data set). After using the original bokeh module 
(which produced variations of a red square as output), the pandas-bokeh module was relatively painless and only required personalisation. 
Once completed the show_figure option could be turned off and the save function (return_html) used instead. 
This used the previously mentioned create_out_dir function, which produced a graphics folder.

#### command_line_script.py

main:
The main function was originally provided by osmart, the lead developer on this project. 
But I felt that there were changes needed in order to meet my requirements for my plans.
Changes included:
- Adding various new functions which added functionality.
- Adding a for loop to control the script for each file downloaded from github.
