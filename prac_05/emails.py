def main():
    my_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        my_dict[email] = name
        email = input("Email: ")

    for email, name in my_dict.items():
        print("{} ({})".format(name, email))


def get_name(email):
    email = email.split('@')[0]
    parts = email.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == '__main__':
    main()
