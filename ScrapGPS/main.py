# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def create_key(name):
    name = name.replace('_', ' ')
    print(name)
    if name.find("-") == 4:
        name_parts = name.split(' ')
        date_reverse = '-'.join(name_parts[0].split('-')[::-1])
        name = date_reverse + ' ' + name_parts[1]
    print(name)
    # if name.count('-') > 3:
    #     name = name[0:name.rfind('-')]
    name = ':'.join(name.rsplit('-', 2))
    return name

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = '2021-02-11_15-06-08'
    print(create_key(name))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
