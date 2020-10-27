def edit_content(contents):
    result = []
    for text in contents:
        result.extend(text.split("\n"))
    return result
