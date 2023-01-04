# transpose-rows2columns
App to transpose .csv that extends past 999+ columns and will write out the columns as rows, and rows to the header columns

The goal is have this app read a .csv and use a module to transpose/covert the header columns to header rows along with the data below the header columns. These .csv files are expected to be 2D such as "Candy name"x "number of candies". 

In such cases, this is best used if the .csv reader/converter app can only display a limited amount of columns about 1000 columns, but can generate more rows to display. For Mac users: Numbers can only display 1000 columns at a time. For Windows users: Excel can display 16384 columns.

This app is written as python code in a virtual environment for testing purposes.