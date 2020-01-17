#!/usr/bin/env python3

import sys
import os.path
import pandas as pd

filevars = {}
with open('output.list', 'r') as f:
    filevars = eval(f.read())
filevars.keys()

df = None
for fname, allvars in filevars.items():
    print(f"Scrubbing {fname}", file=sys.stderr)
    keepvars = allvars[0]
    df = pd.read_stata(fname, columns=keepvars)
    deident_fname = os.path.join(os.path.dirname(fname), "deident_" + os.path.basename(fname))
    df.to_stata(f"{deident_fname}")
