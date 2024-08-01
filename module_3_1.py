calls = 0
def count_calls():
    global calls
    calls += 1


def string_info():
    count_calls()
    string = [len('Capybara'), 'Capybara'.upper(), 'Capybara'.lower()]
    print(tuple(string))
    string = [len('Armageddon'), 'Armageddon'.upper(), 'Armageddon'.lower()]
    print(tuple(string))


def is_contains():
    count_calls()
    string = 'Urban'
    list_to_search = ['ban', 'BaNaN', 'urBAN']
    if any(string.lower() in 'Urban'.lower()for string in list_to_search):
        print(True)
    else:
        print(False)
    string = 'cycle'
    list_to_search = ['recycling', 'cycling']
    if any(string.lower() in 'cycle'.lower() for string in list_to_search):
        print(True)
    else:
        print(False)


string_info()
is_contains()
print(calls)
