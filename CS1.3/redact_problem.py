#!python

def redact(string_array1, string_array2, index=0,final=[]):
    if string_array1[index] not in string_array2:
        final.append(string_array1[index])
    if index >= len(string_array1) -1:
        return final
    return redact(string_array1, string_array2, index+1, final)

if __name__ == "__main__":
    print("redact(['a','b','c','d'],['c','d']) == ['a','b'] Should be True")
    print("Result = {}".format(redact(['a','b','c','d'],['c','d'],0,[]) == ['a','b']))

    print("redact(['a','b','c','d'],[]) == ['a','b','c','d'] Should be True")
    print("Result = {}".format(redact(['a','b','c','d'],[],0,[]) == ['a','b','c','d']))

    print("redact(['a','b','c','d'],['a','b','c','d']) == [] Should be True")
    print("Result = {}".format(redact(['a','b','c','d'],['a','b','c','d'],0,[]) == []))
