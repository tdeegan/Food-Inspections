# Food-Inspections

This program analyzes publicly available data on hundreds of thousands of food inspections using pandas DataFrame objects.

The download-data.py script will download a large file containing food inspection data from the City of Chicago's Data Portal.
Running food_inspections.py will then invoke a "search_by_zip" function and a "search_by_location" function.
Each function accepts a DataFrame containing the original data as an argument.

The "search_by_zip" function returns a DataFrame with rows for restaurants that had a failed inspection since 11/1/16 in ZIP Code 60661.
The "search_by_location" function returns a DataFrame with rows for restaurants that had a failed inspection since 11/1/16 that were within 0.5 mi of a target location.

Each DataFrame object returned from a function is saved as a .csv file.





