import re

def count_words(sentence):
    result = {}
    clean = (' '.join(w.strip("'") for w in sentence.split()).lower())
    clean = re.sub('[\t\n!&@$%^&:.,_]', ' ', clean)

    for word in clean.split():
        word = word.lower()
        word.strip()
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


print(count_words('rah rah ah ah ah\troma roma ma\tga ga oh la la\t'))
