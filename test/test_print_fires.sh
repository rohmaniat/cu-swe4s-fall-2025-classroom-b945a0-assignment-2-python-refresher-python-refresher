test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run print_fires python src/print_fires.py --file_name src/agrofood_data_abbreviated.csv --country "United States of America" --country_column 0 --fires_column 3 --operation "mean"
assert_in_stdout "The nonzero forest fires numbers in United States of America are [1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405].
The sum total of forest fires across all years in United States of America is 59775.
The mean of the forest fire numbers is 1928.225806451613."
assert_exit_code 0

run print_fires python src/print_fires.py --file_name src/agrofood_data_abbreviated.csv --country "Albania" --country_column 0 --fires_column 3 --operation "median"
assert_in_stdout "The nonzero forest fires numbers in Albania are [7, 7, 7, 7, 7, 7, 13, 33, 16, 13, 77, 0, 0, 1, 0, 0, 0, 6, 0, 1, 0, 2, 4, 0, 0, 0, 0, 2, 0, 0, 0].
The sum total of forest fires across all years in Albania is 210.
The median of the forest fire numbers is 1."
assert_exit_code 0

run print_fires python src/print_fires.py --file_name src/agrofood_data_abbreviated.csv --country "Malaysia" --country_column 0 --fires_column 3 --operation "standard deviation"
assert_in_stdout "The nonzero forest fires numbers in Malaysia are [].
The sum total of forest fires across all years in Malaysia is 0.
Unable to calculate stdev"
assert_exit_code 1