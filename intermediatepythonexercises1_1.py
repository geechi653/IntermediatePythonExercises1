def no_duplicates(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

test_list = [1, 2, 3, 1, 1, 3, 4, 5]
print(no_duplicates(test_list))


