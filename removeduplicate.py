def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

duplicate = [2, 3, 42, 3, 2, 10, 20, 1]
print(Remove(duplicate))
