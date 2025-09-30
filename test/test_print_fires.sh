test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run src/run.sh --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3 --operation "mean"
assert_in_stdout "The nonzero forest fires numbers in United States of America are [1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405].
The sum total of forest fires across all years in United States of America is 59775."
assert_exit_code 0

run src/run.sh --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3 --operation "mean"
assert_in_stdout "Error"
assert_exit_code 1