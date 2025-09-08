def get_column(file_name, query_column, query_value, result_column):
    f = open(file_name, 'r') #open the file

    #Splits each line by column
    #Checks if query_column matches query_value
    #If match, it returns the value in result_column
    for line in f:
        columns = line.split(',')
        if columns[query_column] == query_value:
            return columns[result_column]
    else:
        return None
