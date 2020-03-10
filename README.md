![Python application](https://github.com/ARU-Bioinf-ISE/covid19-graphs-DLBPointon/workflows/Python%20application/badge.svg?branch=graph_production)
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
You should get an output like
```
$ covid19_graphs -h
usage: covid19_graphs [-h] [-d] OUT_DIR

tool to download and process COVID-19 data

positional arguments:
  OUT_DIR      directory for output files

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  turn on debug message logging output
```
