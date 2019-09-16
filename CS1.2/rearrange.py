import sys
import random


def do_stuff():
    new_list = list()
    params = sys.argv[1:]
    for i in range(0,len(params)):
        ran_num = random.randint(0,len(params) -1)
        saved = params.pop(ran_num)
        params.append(saved)
    print(params)


if __name__ == "__main__":
    do_stuff()
