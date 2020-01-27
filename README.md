# Quick Consulting Examples

Collection of quick pandas, python, and other coding examples based on real consulting requests.

## JoinMulltipleCSV - How to join multiple CSV files into a single Pandas DataFrame based on a join key.

*Scenario:* Recording student scores for each class lecture, where the student email address and score is stored in a separate CSV file for each lecture.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dlab-berkeley/quick-consulting-examples/master?filepath=JoinMulltipleCSV.ipynb)

## StataFileVariableSearch - How to searching Stata files that contain matching variable names.

*Scenario:* Loop over a directory tree containing Stata .dta files. Read the files into a pandas DataFrame and search for files that contain matching variable names. The result is a dictionary with the Stata filename as the key and the value is the variable names as a list (either full or narrowed just to the matches we're interested in).
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dlab-berkeley/quick-consulting-examples/master?filepath=StataFileVariableSearch.ipynb)

See also the related non-notebook scripts. The [finddta.py](./finddta.py) script essentially is a script-based copy of the notebook version above, and the [scrubdta.py](./scrubdta.py) script takes the output of `finddta.py` as the input for producing a stata file that contains only the columns that match the variables we want to keep, which is useful to de-identify sensitive data.

## Next Example Goes Here...
