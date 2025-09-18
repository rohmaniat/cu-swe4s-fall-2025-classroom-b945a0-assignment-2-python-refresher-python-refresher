import argparse
import my_utils

# Example command to run the script in terminal:
# rohan$ python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3

def print_fires(file_name, country_column, country, fires_column):
    
    print("ciao") #make sure the function is being called
    print(file_name, country_column, country, fires_column) 
    #make sure the arguments are being passed correctly

    # Utilize get_column function from my_utils.py with the input arguments
    fires = my_utils.get_column(file_name, country_column, country, fires_column)

    # Adds together all annual counts found in get_column results
    total_fires = sum((fire) for fire in fires)

    # Print each nonzero annual count of forest fires in the given country
    print("The nonzero forest fires numbers in {} are {}.".format(args.country, fires))

    # Print the sum total of forest fires in the given country across all years
    print("The sum total of forest fires across all years in {} is {}.".format(args.country, total_fires))

if __name__ == "__main__":
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Prints forest fire counts each year in a given country and the number of counts."
    )

    parser.add_argument(
        "--file_name", type=str, default="Agrofood_co2_emission.csv", help="The path to the input file.")
    parser.add_argument(
        "--country", type=str, default="United States of America", help="The country to query.")
    parser.add_argument(
        "--country_column", type=int, default=0, help="The column index for country names.")
    parser.add_argument(
        "--fires_column", type=int, default=3, help="The column index for forest fire counts.")

    # Parse the command-line arguments
    args = parser.parse_args()

    print_fires(args.file_name, args.country_column, args.country, args.fires_column)
