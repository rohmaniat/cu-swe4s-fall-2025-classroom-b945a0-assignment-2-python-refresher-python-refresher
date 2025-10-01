import sys

def get_column(file_name, query_column, query_value, result_column):
    results = []
    try:
        f = open(file_name, 'r') # open the file for reading
    except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return results # exit statement if the file cannot be opened

    # Splits each line by column
    # Checks if query_column matches query_value
    # If match, it returns the value in result_column

    for line in f:
        columns = line.strip().split(',')
        if columns[query_column] == query_value:
            results.append(columns[result_column])

    f.close()

    # Convert the string values to floats first
    for i in range(0 , len(results)):
        try:
            results[i] = float(results[i])
        except ValueError:
            continue
    
    # Then convert the floats to integers
    for i in range(0 , len(results)):
        try:
            results[i] = int(results[i])
        except ValueError:
            continue
    
    return results

def mean (arr):
    # Calculate mean
    try:
        mean_out = sum(arr) / len(arr)
        return mean_out
    except ZeroDivisionError:
        return "Array is empty."
    except TypeError:
        return "Please use floats or strings! :)"
    
def median (arr):
    # Calculate median
    try:
        sorted_arr = sorted(arr)
    except TypeError:
        return "Please use floats or strings! :)"
        
    list_len = len(arr)
    median_place = list_len // 2
    if list_len % 2 == 0:
        return (sorted_arr[median_place - 1] + sorted_arr[median_place]) / 2
    if list_len % 2 == 1:
        return sorted_arr[median_place]
    else:
        return ValueError

def stdev (arr):
    # Calculate standard deviation
    try:
        mean_out = sum(arr) / len(arr)
    except ZeroDivisionError:
        print("Unable to calculate stdev")
        sys.exit(1)
        
    variance = sum((x - mean_out)**2 for x in arr) / len(arr)
    return variance**0.5

if __name__ == "__main__":
    print(get_column("src/agrofood_data_abbreviated.csv", 0, 'United States of America', 3))
# only runs when the file is directly called
# For testing my_utils.py independently
