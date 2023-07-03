def count(input):
    dict_count = {}
    for i in input:
        if i in dict_count:
            dict_count[str(i)] += 1
        else:
            dict_count[str(i)] = 1
    return dict_count

def group_by_key(input):
    dict_group_by = {}
    for dict in input:
        key = dict["key"]
        value = dict["value"]
        if key in dict_group_by:
            dict_group_by[str(key)] += value
        else:
            dict_group_by[str(key)] = value
    return dict_group_by