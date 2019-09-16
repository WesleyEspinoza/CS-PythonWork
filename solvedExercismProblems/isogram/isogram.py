def is_isogram(string):
    if string == '':
        return True
    string = string.lower()
    arr = list()
    for char in string:
        if char not in arr:
            if char.isalpha():
                arr.append(char)
            else:
                continue
        else:
            return False
    return True
