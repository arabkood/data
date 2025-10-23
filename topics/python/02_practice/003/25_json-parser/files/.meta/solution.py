def parseSimpleJSON(json_str):
    json_str = json_str.strip()[1:-1].strip()

    if not json_str:
        return {}

    result = {}
    pairs = json_str.split(',')

    for pair in pairs:
        key_value = pair.split(':')
        key = key_value[0].strip().strip('"')
        value_str = key_value[1].strip()

        if value_str.startswith('"') and value_str.endswith('"'):
            value = value_str.strip('"')
        else:
            value = int(value_str)

        result[key] = value

    return result
