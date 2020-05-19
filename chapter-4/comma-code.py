#!/usr/bin/env python3


spam = ['apples', 'bananas', 'tofu', 'cats']


def main():
    print(concatenate(spam))


def concatenate(name_list):
    string = ""

    for name in name_list[:-1]:
        string += name
        string += ", "

    string += "and "
    string += name_list[-1]


    return string


if __name__ == '__main__':
    main()
