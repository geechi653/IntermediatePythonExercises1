def combine_dicts(dict1, dict2):
    new_dict = {}
    for key in dict1.keys():
        if key in dict2.keys():
            new_dict[key] = dict1[key] + dict2[key]
    return new_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'd': 6}
print(combine_dicts(dict1, dict2))
