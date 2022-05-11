# Quick Consulting Examples

Collection of quick pandas, python, R, and other coding examples based on real consulting requests.

## VoltStats Data Archive - Webscraping example

*Scenario:* This is an example of webscraping a website that containts 10 years of historical user-generated data that used OnStar to collect data about the performance of Chevy Volts driving in the real world. [![Datahub](https://img.shields.io/badge/launch-datahhub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2Fquick-consulting-examples&urlpath=tree%2Fquick-consulting-examples%2FVolt%20Stats%20solution%20in%20Python.ipynb&branch=master)


## Geopandas Discovery Project Example - How to create a heat map using geopandas

*Scenario:* This is an example consulting request from a [Discovery project](https://data.berkeley.edu/research/discovery-program-home) by an Undergraduate Student from Econ and Data Science requesting help with Data Visualization as a Debugging or Tech support request saying: "I would like to create a geopandas heat map of India (with coordinates and a legend of certain levels of GDP per capita), but I've never used geopandas before so a little unsure on how to create this mapping. Also unsure if I need to convert to a shape file."
[![Datahub](https://mybinder.org/badge_logo.svg)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2Fquick-consulting-examples&urlpath=tree%2Fquick-consulting-examples%2FGeopandas+Discovery+Project+Example.ipynb&branch=master)


## JoinMulltipleCSV - How to join multiple CSV files into a single Pandas DataFrame based on a join key.

*Scenario:* Recording student scores for each class lecture, where the student email address and score is stored in a separate CSV file for each lecture.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dlab-berkeley/quick-consulting-examples/master?filepath=JoinMulltipleCSV.ipynb)

## StataFileVariableSearch - How to search Stata files that contain matching variable names.

*Scenario:* Loop over a directory tree containing Stata .dta files. Read the files into a pandas DataFrame and search for files that contain matching variable names. The result is a dictionary with the Stata filename as the key and the value is the variable names as a list (either full or narrowed just to the matches we're interested in).
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dlab-berkeley/quick-consulting-examples/master?filepath=StataFileVariableSearch.ipynb)

See also the related non-notebook scripts. The [finddta.py](./finddta.py) script essentially is a script-based copy of the notebook version above, and the [scrubdta.py](./scrubdta.py) script takes the output of `finddta.py` as the input for producing a stata file that contains only the columns that match the variables we want to keep, which is useful to de-identify sensitive data.

## Crop-spatial-points-with-shapefile - take a raw dataset of spatial points and initialize the CRS, and then crop with a shapefile. 

*Scenario:* You are presented with a large spatial dataset of floral species in the continental United States. The researcher is only concerned with data mapped into the boundaries of the state of Florida. Dataset is presented without a Coordinate Reference System. Format the raw spatial data with a CRS, and use a shapefile of the state of Florida to crop only the points that land within its boundary. 

## Lasso-Variable-Importance - use tidymodels framework to structure, preprocess, and tune hyperparameters for a lasso regression analysis

*Scenario:* A student is hoping to run a lasso regression analysis on some data for their final project in a class. They have been working with the `glmnet` package but have encountered errors when formatting data for model preparation. Walk through the process of splitting and model preparation of data, along with bootstrapping and tuning grid approaches to hyperparameter optimization. use `vip` package to visualizing feature importance from `tidymodels` object. 

## Network-Analysis-Visualization - How to visualize a social network with contact tracing data.

*Scenario:* Take a dataset recording "relationships" between cases and contacts during a COVID19 outbreak, implement complex `join` functions to wrangle and format dataframes to be handled by the `VisNetwork` package. Use the formatted dataframes to create an interactive html object that illustrates acyclic exposure events from cases to contacts. 



## Next Example Goes Here...
