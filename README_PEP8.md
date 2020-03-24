# Python code compliance

## Instructions

This must be assessed by the pycodestyle and pylint tools. 
Please note your code must conform to the 79 characters line length limit. 
You must use the `pycodestyle` and `pylint` tools and include the output for 
all python code in this file `README_PEP8.md`. 

pycodestyle should not produce any warnings.

It is acceptable to have pylint warnings (for instance missing docstrings for unit tests)
 provided they are justified in README_PEP8.md..

## `pycodestyle *.py` output
```
(base) mib113629i:covid19-graphs-DLBPointon dp24$ pycodestyle covid19_graphs/covid19_processing.py
(base) mib113629i:covid19-graphs-DLBPointon dp24$ 
```
No output from PyCodeStyle on covid19_processing.py or command_line_script.py

## `pylint *.py` output
```
************* Module command_line_script
(base) mib113629i:covid19-graphs-DLBPointon dp24$ pylint covid19_graphs/command_line_script.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.26/10, +0.74)

************* Module covid19_processing
covid19_graphs/covid19_processing.py:107:4: R0914: Too many local variables (33/15) (too-many-locals)
covid19_graphs/covid19_processing.py:227:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
covid19_graphs/covid19_processing.py:107:4: R0912: Too many branches (35/12) (too-many-branches)
covid19_graphs/covid19_processing.py:107:4: R0915: Too many statements (83/50) (too-many-statements)
covid19_graphs/covid19_processing.py:377:4: R0914: Too many local variables (20/15) (too-many-locals)
covid19_graphs/covid19_processing.py:9:0: W0611: Unused import pandas_bokeh (unused-import)

------------------------------------------------------------------
Your code has been rated at 9.72/10 (previous run: 9.72/10, +0.00)

```

## Justifications for pylint warnings

- W0611: Unused import: This is to be ignored, the import is essential to the use of the
bokehplot function in covid19_processing.py

- R0914 - Not Justified - Could have been simplified by the use of a dictionary rather than a large number of lists.

- R1702 - This is required to sort the countries in to their respective regions
found in the original CSV's

- R0915 - Not Justified - could be fixed by splitting the data function into multiple functions, but this would require significant work.

- R0912 - See above.