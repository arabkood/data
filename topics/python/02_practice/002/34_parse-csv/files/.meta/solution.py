def parseCSV(headers, values):
    header_list = headers.split(",")
    value_list = values.split(",")
    result = {}

    for i in range(len(header_list)):
        result[header_list[i]] = value_list[i]

    return result
