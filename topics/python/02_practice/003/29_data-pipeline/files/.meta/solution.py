def pipeline(data, transforms):
    result = data
    for transform in transforms:
        result = transform(result)
    return result
