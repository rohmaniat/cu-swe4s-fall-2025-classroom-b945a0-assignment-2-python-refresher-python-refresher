# python-refresher

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)

## my_utils.py

Includes the get_column function
Inputs: **file_name**, **query_column**, **query_value**, **result_column**
Opens a given file **file_name**.
Looks in a column **query_column** for all instances of **query_value**.
Each time a value in **query_column** matches **query_value**, the value in the **result_column** in the same row is called.
Adds the value in the **result_column** to the results array.
Converts all values in the results array to floats, then to integers

Contains a main function that tests the get_column function for parameters ("Agrofood_co2_emission.csv", 0, 'United States of America', 3)

Contains functions to calculate the mean, median, and standard deviation for an array of integers or floats.

## print_fires.py

uses the get_column function in my_utils.py to output all entries for the number of annual forest fires for a given country

Allows you to pass arguments for the following:

--file_name (default = 'Agrofood_co2_emission.csv')
--country_column ("query_column" in my_utils, default = 0)
--country ("query_value" in my_utils, default = "United States of America")
--fires_column ("result_column in my_utils, default = 3)
--operation ("mean" "median" "standard deviation", calculates one of these for all values outputted, default = None)

Outputs:

The nonzero forest fires numbers in (country) are (list of forest fire counts).

The sum total of forest fires across all years in (country) is (sum of forest fire counts).

The (operation) of these numbers is (mean/median/stdev).

## run.sh

shell script file that runs
> python3 print_fires.py
with multiple sets of arguments

--file_name src/agrofood_data_abbreviated.csv --country "United States of America" --country_column 0 --fires_column 3
    this one works

## Unittest_meanmedstdev

Unit tests for mean, median, and standard deviation operations

- tests simple operations with round numbers
- tests that mean and median are between the min and max of the array
- tests that standard deviation is greater than zero
- tests all three operations against the similar function from NumPy library
- uses randomized inputs (1000 iterations) for rigor

## test_print_fires.sh

Functional tests for run.sh that runs the print_fires file

uses the Stupid Simple Bash Commands (SSSH) framework
