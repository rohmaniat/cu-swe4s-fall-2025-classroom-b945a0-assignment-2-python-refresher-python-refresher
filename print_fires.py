# Assign all vars for my_utils.py get_column function
file_name = 'Agrofood_co2_emission.csv'
country= 'United States of America'
country_column = 0 # column 0 == "Area"
fires_column = 3 # column 3 == "Forest fires"

# Import get_column function from my_utils.py
import my_utils
get_column = my_utils.get_column

fires = get_column(file_name, country_column, country, fires_column)
total_fires = sum(float(fire) for fire in fires)

# Print each nonzero annual count of forest fires in the given country
print("The nonzero forest fires numbers in {} are {}.".format(country, fires))

# Print the sum total of forest fires in the given country across all years
print("The sum total of forest fires across all years in {} is {}.".format(country, total_fires))


