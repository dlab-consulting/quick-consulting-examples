import fnmatch
import os
import os.path
import re

#startdir = '.' # by default start "here" in current directory
startdir = '/home/prisoner/data'
#startdir = '/home/prisoner/data/analysis/casenoteaddresses'
includes = ['*.dta'] # for files only
excludes = [] # for dirs and files

# transform glob patterns to regular expressions
includes = r'|'.join([fnmatch.translate(x) for x in includes])
excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

dtafiles = []
for root, dirs, files in os.walk(startdir):

    # exclude dirs
    dirs[:] = [os.path.join(root, d) for d in dirs]
    dirs[:] = [d for d in dirs if not re.match(excludes, d)]

    # exclude/include files
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if not re.match(excludes, f)]
    files = [f for f in files if re.match(includes, f)]

    for fname in files:
        #print(fname)
        dtafiles.append(fname)

import pandas as pd

# using a dictionary comprehension to iterate over all stata files to read as a pandas dataframe
# and generate a dictionary with filename as key and variable list as values
# https://python-reference.readthedocs.io/en/latest/docs/comprehensions/dict_comprehension.html
allvars = {fname : pd.read_stata(fname, iterator=True).varlist for fname in dtafiles}
allvars

# Similar to above, but we ignore any variables not in our match list using set intersection.
#
# filter files to just the subset that matches the list of variables we are interested in
# and generate a dictionary with filename as key and the NARROWED variable list in that file
matches = ['arc_street','x','y','stan_addr','match_addr','adrs']
files_with_matching_variables_filtered = {fname : set(matches).intersection(variables) for fname,variables in allvars.items() if any(elem in matches for elem in variables)}
print(files_with_matching_variables_filtered)
