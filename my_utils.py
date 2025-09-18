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

if __name__ == "__main__":
    print(get_column('/Users/rohan/local_coding/assignment-2-python-refresher-rohmaniat/Agrofood_co2_emission.csv', 0, 'United States of America', 3))
# only runs when the file is directly called
# For testing my_utils.py independently
