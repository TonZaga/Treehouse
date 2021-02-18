# def remember(thing):
#     # open file
#     file = open("database.txt", "a")
#     # write thing to file
#     file.write(thing+"\n")
#     # close file
#     file.close()


# if __name__ == '__main__':
#     remember(input("What should I remember? "))



# def remember(thing):
#     # open file
#     with open("database.txt", "a") as file:
#     # write thing to file
#         file.write(thing+"\n")


# if __name__ == '__main__':
#     remember(input("What should I remember? "))


import sys


def remember(thing):
    # open file
    with open("database.txt", "a") as file:
    # write thing to file
        file.write(thing+"\n")


def show():
    # open file
    with open("database.txt") as file:
        for line in file:
            print(line)

if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remember(' '.join(sys.argv[1:]))
