def get_column(file_name, query_column, query_value, result_column = 1):
    results = []
    try:
        f = open(file_name, 'r') # open the file
    except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            return results # exit statement if the file cannot be opened

    # Splits each line by column
    # Checks if query_column matches query_value
    # If match, it returns the value in result_column

    for line in f:
        columns = line.strip().split(',')
        if columns[query_column] == query_value:
            results.append(int(columns[result_column]))

    f.close()
    return results

print(get_column('/Users/rohan/local_coding/assignment-2-python-refresher-rohmaniat/Agrofood_co2_emission.csv', 0, 'United States of America', 3))

