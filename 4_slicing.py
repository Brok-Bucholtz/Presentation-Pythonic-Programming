import copy


def splits():
    example_list = [1, 2, 3, 4, 5]
    print(example_list[:2])
    print(example_list[2:])
    print(example_list[1:4])


def strides():
    example_list = [1, 2, 3, 4, 5]
    print(example_list[1:4:2])
    print(example_list[::2])
    print(example_list[::-1])


def assign_slice():
    example_list = [1, 2, 3, 4, 5]

    # Replace
    test_list = copy.deepcopy(example_list)
    test_list[1:3] = [-1, -1]
    print(test_list)

    # Insert
    test_list = copy.deepcopy(example_list)
    test_list[1:1] = [9, 9]
    print(test_list)

    # Remove
    test_list = copy.deepcopy(example_list)
    test_list[1:4] = []
    print(test_list)


if __name__ == '__main__':
    print('splits')
    splits()
    print('\nstrides')
    strides()
    print('\nassign_slice')
    assign_slice()
