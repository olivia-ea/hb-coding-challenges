def translate_to_binary(s):

    vowels = ['a','e','i','o','u']

    string = list(s)

    binary_string = []
    
    for letter in string:
        if letter in vowels:
            binary_string.append('0')
        else:
            binary_string.append('1')

    return ''.join(map(str, binary_string))


def find_binary_match(pattern, s):

    binary_string = translate_to_binary(s)

    return binary_string.count(pattern)

