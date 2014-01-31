SF1_2010
===========

First - Point pythonDL to the correct census ftp library to pull what you need, if you need all of the census data.

Second - Unzip the sf1 text files

Third - CensusSF1.py to create csv's

Fourth - run geoRipper.py on the geo file.  Remove the headers.

Fifth - open the create_table_sql to make the appropriate table for the state you are doing

Sixth - import the CSV after manually deleting headers