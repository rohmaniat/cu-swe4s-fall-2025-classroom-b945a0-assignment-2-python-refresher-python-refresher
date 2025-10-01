import argparse
import my_utils

# Example command to run the script in terminal:
# rohan$ python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3

def print_fires(file_name, country_column, country, fires_column, operation):
    
    print(file_name, country_column, country, fires_column) 
    #make sure the arguments are being passed correctly

    # Utilize get_column function from my_utils.py with the input arguments
    fires = my_utils.get_column(file_name, country_column, country, fires_column)

    # Adds together all annual counts found in get_column results
    total_fires = sum((fire) for fire in fires)

    # Print each nonzero annual count of forest fires in the given country
    print("The nonzero forest fires numbers in {} are {}.".format(country, fires))

    # Print the sum total of forest fires in the given country across all years
    print("The sum total of forest fires across all years in {} is {}.".format(country, total_fires))

    if operation == "mean":
        mean = my_utils.mean(fires)
        print("The mean of the forest fire numbers is {}.".format(mean))

    if operation == "median":
        median = my_utils.median(fires)
        print("The median of the forest fire numbers is {}.".format(median))

    if operation == "standard deviation":
        stdev = my_utils.stdev(fires)
        print("The standard deviation of the forest fire numbers is {}.".format(stdev))

if __name__ == "__main__":
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Prints forest fire counts each year in a given country and the number of counts."
    )

    parser.add_argument(
        "--file_name", type=str, default="src/agrofood_data_abbreviated.csv", 
        help="The path to the input file.")
    parser.add_argument(
        "--country", type=str, default="United States of America", 
        help="The country to query.")
    parser.add_argument(
        "--country_column", type=int, default=0, 
        help="The column index for country names.")
    parser.add_argument(
        "--fires_column", type=int, default=3, 
        help="The column index for forest fire counts.")
    parser.add_argument(
        "--operation", type=str, default= None, 
        help="Optionally indicate if you would like the mean, median, or standard deviation of the values")

    # Parse the command-line arguments
    args = parser.parse_args()

    print_fires(args.file_name, args.country_column, args.country, args.fires_column, args.operation)
