#!/usr/bin/env python3

import fnmatch
import os
import os.path
import re
import sys
import pandas as pd
from fuzzywuzzy import process
from ordered_set import OrderedSet
import pprint

startdir = '/home/prisoner/data'
#startdir = '/home/prisoner/data/analysis/casenoteaddresses'

if not os.path.exists(startdir):
	startdir = '.' # by default start "here" in current directory if directory does not exist

print(f"Searching in directory: {startdir}", file=sys.stderr)

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

# iterate over all stata files to read as a pandas dataframe
# and generate a dictionary with filename as key and variable list as values
# handling any corrupted file errors by logging to error.log and moving on
allvars = {}
with open('error.log', 'w') as log:
    for fname in dtafiles:
        try:
            allvars[fname] = pd.read_stata(fname, iterator=True).varlist
        except:
            print("Corrupt file:", fname, file=sys.stderr)
            print(fname, file=log)

# This version outputs the FULL list of variables as a list of lists (matches,
# then todrop) since that will be helpful to see which variables were included
# and excluded in the fuzzy match
#
# filter files to just the subset that matches the list of variables we are
# interested in based on fuzzy matching and then generate a dictionary with
# filename as key and the matching variable list in that file
#
# This also uses fuzzy variable matching with a tuneable threshold value between 0-100.
threshold = 90
choices = ['arc_street','x','y','stan_addr','match_addr','adrs']
matches = []
files_with_matching_variables = {}
for fname,variables in allvars.items():
    list_of_lists = [process.extract(a, variables, limit=None) for a in choices]
    flattened = [val for sublist in list_of_lists for val in sublist]
    matches = OrderedSet([a for a,b in flattened if b>=threshold])
    todrop = OrderedSet(variables) - matches
    if matches:
        files_with_matching_variables[fname] = [list(matches), list(todrop)]
pp = pprint.PrettyPrinter(compact=True)
pp.pprint(files_with_matching_variables)
