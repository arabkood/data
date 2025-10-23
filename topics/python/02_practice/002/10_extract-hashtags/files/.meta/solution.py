def extractHashtags(text):
    words = text.split()
    hashtags = []

    for word in words:
        if word.startswith("#") and len(word) > 1:
            # Remove the # and any non-alphanumeric characters at the end
            tag = ""
            for char in word[1:]:
                if char.isalnum():
                    tag += char
                else:
                    break
            if tag:
                hashtags.append(tag)

    return hashtags
