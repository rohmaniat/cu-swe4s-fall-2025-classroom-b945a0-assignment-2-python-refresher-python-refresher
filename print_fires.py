import argparse
import my_utils

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Prints forest fire counts each year in a given country and the number of counts."
)
parser.add_argument("file_name", type=str, help="The path to the input file.")
parser.add_argument("country", type=str, help="The country to query.")
parser.add_argument("country_column", type=int, default=0, help="The column index for country names.")
parser.add_argument("fires_column", type=int, default=3, help="The column index for forest fire counts.")

# Parse the command-line arguments
args = parser.parse_args()

# Utilize get_column function from my_utils.py with the input arguments
fires = my_utils.get_column(
    args.file_name, args.country_column, args.country, args.fires_column
)

# Adds together all annual counts found in get_column results
total_fires = sum(float(fire) for fire in fires)

# Print each nonzero annual count of forest fires in the given country
print("The nonzero forest fires numbers in {} are {}.".format(args.country, fires))

# Print the sum total of forest fires in the given country across all years
print("The sum total of forest fires across all years in {} is {}.".format(args.country, total_fires))


