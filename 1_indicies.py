def zip_example():
    example_numbers = [1, 2, 3]
    example_letters = ['a', 'b', 'c']

    for number, letter in zip(example_numbers, example_letters):
        print('Number: {} Letter: {}'.format(number, letter))


def enumerate_example():
    example_letters = ['a', 'b', 'c']

    for example_i, letter in enumerate(example_letters):
        print('Example i: {} Letter: {}'.format(example_i, letter))


def second_letters():
    example_letters = ['a', 'b', 'c', 'd', 'e', 'f']

    for second_letter in example_letters[::2]:
        print('Second Letter: {}'.format(second_letter))


if __name__ == '__main__':
    print('zip_example')
    zip_example()
    print('\nenumerate_example')
    enumerate_example()
    print('\nsecond_letters')
    second_letters()
