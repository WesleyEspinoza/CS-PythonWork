import sys

def reverse_input(text):
    new_word_order = []
    for _ in range(0,len(text)):
        saved = text.pop()
        new_word_order.append(saved)
    print(' '.join(new_word_order))
if __name__ == "__main__":
    params = sys.argv[1:]

    reverse_input(params)
