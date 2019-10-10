insert_index_set = set()
M = 13


def h(key, M=13):
    return key % M


to_insert = [765, 431, 96, 142, 579, 226, 903, 388]
for number in to_insert:
    index = h(number)
    first_index = index
    i = 1
    while index in insert_index_set:
        print(f'h{number} = {number} %  M = {index}')
        index = (first_index + i*i) % M
        i += 1
    else:
        print(f'h{number} = {number} %  M = {index}')
        insert_index_set.add(index)





