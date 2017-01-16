def list_comprehen():
    example_list = [x*3 for x in range(5)]
    print(example_list)


def dict_comprehen():
    example_dict = {x: x/2 for x in range(5)}
    print(example_dict)


def filter_list():
    filter = [1, 3, 5, 6, 7, 8]
    filtered_list = [x for x in range(10) if x not in filter]

    print(filtered_list)


if __name__ == '__main__':
    print('list_comprehen')
    list_comprehen()
    print('\ndict_comprehen')
    dict_comprehen()
    print('\nfilter_list')
    filter_list()
