MIN_PASSWORD_LENGTH = 8


def main():
    password = input("Input a password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Please input a password greater than {0} characters".format(MIN_PASSWORD_LENGTH))
        password = input("Input a password: ")
    print("Your password is: {0}".format('*' * len(password)))


if __name__ == "__main__":
    main()
