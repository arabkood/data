def renderTemplate(template, data):
    result = template

    for key, value in data.items():
        placeholder = "{{" + key + "}}"
        result = result.replace(placeholder, str(value))

    import re
    result = re.sub(r'\{\{[^}]+\}\}', '', result)

    return result
