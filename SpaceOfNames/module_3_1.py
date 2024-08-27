calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(args):
    count_calls()
    tuple_ = (len(args), args.upper(), args.lower())
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    for element in list_to_search:
        if string.upper() == element.upper():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
