def main():
    get_name()


def get_name():
    name = input("What is your name: ")
    method_name(name)


def method_name(name):
    while not name:
        name = input("Enter a valid name: ")
    print(name[::2])


main()