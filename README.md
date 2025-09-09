# python-refresher

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)

## my_utils.py

Includes the get_column function
Inputs: **file_name**, **query_column**, **query_value**, **result_column (default = 1)**
Opens a given file **file_name**.
Looks in a column **query_column** for all instances of **query_value**.
Each time a value in **query_column** matches **query_value**, the value in the **result_column** in the same row is called.
Adds the value in the **result_column** to the results array.

## print_fires.py

uses the get_column function in my_utils.py to output all entries for the number of annual forest fires for a given country
file_name = 'Agrofood_co2_emission.csv'
query_column = 0 (labeled as "country_column")

## run.sh

shell script file that runs print_fires.py
