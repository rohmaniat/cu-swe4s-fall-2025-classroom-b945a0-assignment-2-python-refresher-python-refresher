#!/bin/bash

# This one will work
python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3

# chmod +x run.sh 
# to make the code executable
# ./run.sh to run the code

# This one will not work
# The csv file name is spelled wrong
python3 print_fires.py --file_name Agrofood_co2_emision.csv --country "United States of America" --country_column 0 --fires_column 3

# This one will not work
# Fires_column index is a float instead of an integer
python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 4.5