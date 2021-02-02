#-----------------------------------------------------------------------## Intro to Python #
#-----------------------------------------------------------------------#

# SERVICE_CHARGE = 2
# TICKET_PRICE = 10

# tickets_remaining = 100

# # Create the calculate price function.  It takes number of tickets and returns
# # num_tickets * TICKET_PRICE
# def calculate_price(number_of_tickets):
#     return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# while tickets_remaining >= 1:
#     print("There are {} tickets remaining.".format(tickets_remaining))
#     name = input("What is your name?  ")
#     num_tickets = input("How many tickets would you like, {}?".format(name))
#     try:
#         num_tickets = int(num_tickets)
#         if num_tickets > tickets_remaining:
#             raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
#     except ValueError as err:
#         print("Oh no, we ran into an issue. {}.  Please try again.".format(err))
#     else:
#         amount_due = calculate_price(num_tickets)
#         print("The total due is {}.".format(amount_due))
#         should_proceed = input("Do you want to proceed?  Y/N  ")
#         if should_proceed.lower() == "y":
#             # TODO: gather credit card info and process
#             print("SOLD!")
#             tickets_remaining -= num_tickets
#         else:
#             print("Thank you anyways, {}!".format(name))
# print("Sorry the tickets are all sold out. :(")

#-----------------------------------------------------------------------#
# Practice Input and Output #
#-----------------------------------------------------------------------#

# MadLibs - Practice Input and Output
#
# Template:
#   I enjoy practice!  I find it helps me to __(Verb)__ better.
#   Without practice, my __(noun)__ would probably not even work.
#   My code is getting more __(adjective)__ every single day!

# TODO: Prompt the user for parts of speech and store them in varibles
# verb = input("Please enter a verb: ")
# noun = input("Please enter a noun: ")
# adjective = input("Please enter an adjective: ")



# # TODO: Output the template to the screen with the blanks filled out with what user stated

# print(f"I enjoy practice!  I find it helps me to {verb} better.  Without practice, my {noun} would probably not even work.  My code is getting more {adjective} every single day!")


#-----------------------------------------------------------------------#
# Introducing Lists #
#-----------------------------------------------------------------------#

# attendees = ["Ken", "Alena", "Treasure"]
# attendees.append("Ashley")
# attendees.extend(["James", "Guil"])
# optional_invitees = ["Ben", "Dave"]
# potential_attendees = attendees + optional_invitees
# print("Ther are", len(potential_attendees), "potential attendees currently")





# books = [
#     "Learning Python: Powerful Object-Oriented Programming"
#     "Automated the Boring stuff with Python",
#     "Python for Data Analysis",
#     "Fluent Python: Clear, Concise, and Effective Python",
#     "Python for kids",
#     "Hello Web App: Lear how to build a web app"
# ]

# print("Suggested gift: {}".format(books[0]))





# video_games = [
#     "Call of Duty: Black Ops Cold War",
#     "World of Warcraft",
#     "Escape from Tarkov"
# ]

# print("Video Games:")
# for game in video_games:
#     print("* " + game)


# def display_wishlist(display_name, wishes):
#     items = wishes.copy()
#     print(display_name + ":")
#     suggested_gift = items.pop(0)
#     print("======>", suggested_gift, "<======")
#     for item in items:
#         print("* " + item)
#         print()

# display_wishlist("Books", books)
# display_wishlist("Video Games", video_games)





# travel_expenses = [
#     [5.00, 2.75, 22.00, 0.00, 0.00],
#     [24.75, 5.50, 15.00, 22.00, 8.00],
#     [2.75, 5.50, 0.00, 29.00, 5.00]
# ]

# print("Travel Expenses:")
# week_number = 1
# for week in travel_expenses:
#     print("* Week #{}: ${}".format(week_number, sum(week)))
#     week_number += 1





# shopping_list = []

# def show_help():
#     print("What should we pick up at the store?")
#     print("""
# Enter 'DONE' to stop adding items.
# Enter 'HELP' for this help.
# ENTER 'SHOW' to see your current shopping list.
# """)


# def add_to_list(item):
#     shopping_list.append(item)
#     print("Item was added.  Currently {} in the list.".format(len(shopping_list)))


# def show_list():
#     print("Current shopping list:")
#     for item in shopping_list:
#         print(item)

# show_help()
# while True:
#     new_item = input("> ")

#     if new_item == "DONE":
#         break
#     elif new_item == "HELP":
#         show_help()
#         continue
#     elif new_item == "SHOW":
#         show_list()
#         continue

#     add_to_list(new_item)

# show_list()


#-----------------------------------------------------------------------#
# Practice Writing loops in python #
#-----------------------------------------------------------------------#

# BIRTHDAYS = (
#     ("James", "9/8", True, 9),
#     ("Shawna", "12/6", True, 22),
#     ("Amaya", "28/2", False, 8),
#     ("Kamal", "29/4", True, 19),
#     ("Sam", "16/7", False, 22),
#     ("Xan", "14/3", False, 34),
# )

# print("Celebrations:")
# for person in BIRTHDAYS:
#     if person[2]:
#         print("Happy birthday, {}!!".format(person[0]))


# Half birthdays #
# print("Half birthdays:")

# for person in BIRTHDAYS:
#     name = person[0]
#     birthdate = person[1].split('/')
#     birthdate[1] = int(birthdate[1]) + 6
#     if birthdate[1] > 12:
#         birthdate[1] -= 12
#     birthdate[1] = str(birthdate[1])
#     print(name, "/".join(birthdate))



# School birthdays #
# print("School birthdays:")

# for person in BIRTHDAYS:
#     name = person[0]
#     birthdate = person[1].split('/')
#     birthdate[1] = int(birthdate[1])
#     if birthdate[1] in range(1, 7) or birthdate in range(9, 13):
#         print(name)


# Stars #
# for person in BIRTHDAYS:
#     name = person[0]
#     age = person[-1]
#     celebrates = person[-2]

#     if celebrates and age <= 10:
#         stars = ''
#         for star in range(age):
#             stars += '*'
#         print(name, stars)



# Warm oven #
# current_oven_temp = 75

# while current_oven_temp < 350:
#     current_oven_temp += 25
#     print(current_oven_temp)
# else:
#     print("The oven is ready!")



# Total and average #
# def total_and_average():
#     numbers = []
#     while True:
#         num = input("Give me a number, or 'q' to quit: ").lower()
#         if num == 'q':
#             break
#         try:
#             numbers.append(float(num))
#         except ValueError:
#             continue
#     print("You entered: ", numbers)
#     print("The total is: ", sum(numbers))
#     print("The average is: ", sum(numbers)/len(numbers))

# total_and_average()


# Missbuzz #
# current = 1

# while current < 101:
#     if not current % 3 or current % 5 == 0:
#         print(current)
#     current += 1


#-----------------------------------------------------------------------#
# Practice Comparsions in python #
#-----------------------------------------------------------------------#

# name = input("Please enter your name: ")
# number = input("Please enter a number: ")
# number = int(number)
    
# is_fizz = number % 3 == 0
# is_buzz = number % 5 == 0

# print("Hey, {}!\nYour number is {}".format(name, number))

# if is_fizz and is_buzz:
#     print("{} is a FizzBuzz number.".format(number))
# elif is_fizz:
#     print("{} is a Fizz number.".format(number))
# elif is_buzz:
#     print("{} is a Buzz number.".format(number))
# else:
#     print("{} is neither a fizzy or a buzzy number".format(number))



#-----------------------------------------------------------------------#
# Practice Comparsions in python #
#-----------------------------------------------------------------------#


# name = input("What is your name? ")
# year = input("What year were you born? ")

# while True:
#     try:
#         year = int(year)
#     except ValueError:
#         continue
#     else:
#         break

# # Step 2
# # Calculate and print the year they'll turn 25, 50, 75, and 100.
# current_year = 2020
# current_age = current_year - year
# turn_25 = (25-current_age) + current_year
# turn_50 = (50-current_age) + current_year
# turn_75 = (75-current_age) + current_year
# turn_100 = (100-current_age) + current_year
# # Step 3
# # If they're already past any of these ages, skip them.
# if turn_25 > current_year:
#     print("{}, you'll turn 25 in the year {}!".format(name, turn_25))
# if turn_50 > current_year:
#     print("{}, you'll turn 50 in the year {}!".format(name, turn_50))
# if turn_75 > current_year:
#     print("{}, you'll turn 75 in the year {}!".format(name, turn_75))
# if turn_100 > current_year:
#     print("{}, you'll turn 100 in the year {}!".format(name, turn_100))



#-----------------------------------------------------------------------#
# Practice Using Strings and Lists in python #
#-----------------------------------------------------------------------#

# # Step 1:
# # Make two strings, each should be 8 characters long, made up of Xs and Os.
# # First string should start with X, second string should start with O.
# # Both strings should alternate between the two characters.
# # You can use multiplication for this.

# xo = 'xo' * 4
# ox = 'ox' * 4

# # Step 2:
# # Make a list
# # Add 1 of the X-started strings.
# # Add 1 of the O-started strings.
# # Repeat until you have 8 items total in the list.
# # You can use multiplication for this, too.

# xoxo = [xo, ox] * 4

# # Step 3:
# # Print out the list of strings, joined with newlines \n.

# print('\n'.join(xoxo))


#-----------------------------------------------------------------------#
# Practice Creating and indexing lists in python #
#-----------------------------------------------------------------------#

# # TODO Create an empty list to maintain the player names
# players = []

# # TODO Ask the user if they'd like to add players to the list.
# # If the user answers "Yes", let them type in a name and add it to the list.
# # If the user answers "No", print out the team 'roster'
# add_player = input("Would you like to add a player to your team? (Yes/No)")
# while add_player.lower() == 'yes':
#     name = input("\nEnter the name of the player to add to the team: ")
#     players.append(name)
#     add_player = input("Would you like to add another player to your team?")

# # TODO print the number of players on the team
# print("\nThere are {} players on the team.".format(len(players)))

# # TODO Print the player number and the player name
# # The player number should start at the number one
# player_number = 1
# for player in players:
#     print("Player {}: {}".format(player_number, player))
#     player_number += 1

# # TODO Select a goalkeeper from the above roster
# keeper = input("Please select the goal keeper by selecting the player number. (1-{})".format(len(players)))

# keeper = int(keeper)

# # TODO Print the goal keeper's name
# # Remember that lists use a zero based index
# print("Great! The goalkeeper for the game will be {}".format(players[keeper -1]))


#-----------------------------------------------------------------------#
# Introducing Tuples in python # *list but one key difference (immutable)
#-----------------------------------------------------------------------#

# A list
# groceries = ['apples', 'oranges', 'lettuce', 'cheddar cheese']

# A tuple 
# with non brackets []
# groceries = 'apples', 'oranges', 'lettuce', 'cheddar cheese'

# Also a tuple 
# with parentheses for readability
# groceries = ('apples', 'oranges', 'lettuce', 'cheddar cheese')



#-----------------------------------------------------------------------#
# Functions, packing, and unpacking in python #
#-----------------------------------------------------------------------#

# def print_name():
#     print("Anthony")

# def favorite_movie():
#     print("Blank Check")

# print_name()
# favorite_movie()

#

# num = 10

# def set_num():
#     num = 5
#     print(num)

# set_num()

#

# def two_plus_two():
#     val = 2 + 2
#     return val

# sum = two_plus_two()
# print(sum)

# print(two_plus_two() * 2)


# def add_two(num):
#     print(num)
#     val = num + 2
#     return val

# print(add_two(10))


# def add_two_nums(num1, num2):
#     val = num1 + num2
#     return val

# print(add_two_nums(5, 10))

# def multi_values(num1, num2):
#     val = num1 * num2
#     return val

# print(multi_values(5, 10))


#


# def packer(arg1, arg2, arg3, arg4):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#     print(arg4)

# packer('Hi', 'i', 'love', 'python')


# def packer(*args):
#     print(args)

# packer('Hi', 'i', 'love', 'python')


# def packer(*args):
#     for val in (args):
#         print(val)

# packer('Hi', 'i', 'love', 'python')


# def calculate_total(*args):
#     total = sum(args)
#     print(total)

# calculate_total(25, 25, 20, 30)


# def unpacker():
#     return (1, 2, 3)

# var1, var2, var3 = unpacker()

# print(var1)
# print(var2)
# print(var3)


# def unpacker():
#     return ('hey')

# var1, var2, var3 = unpacker()

# print(var1)
# print(var2)
# print(var3)


#

# full_name = input("Enter your full name: \n").split (' ')

# print(full_name)


# first, last = input("Enter your full name: \n").split (' ')

# print(first)
# print(last)



#-----------------------------------------------------------------------#
# Python Sequences #
#-----------------------------------------------------------------------#

# my_name = "Anthony"
# for letter in my_name:
#     print(letter)


# grocery = ["roast beef", "cucumbers", "lettuce", "peanut butter", "bread", "dog food"]

# index = 1
# for item in grocery:
#     print(f"{index}. {item}")
#     index += 1


# grocery = ["roast beef", "cucumbers", "lettuce", "peanut butter", "bread", "dog food"]

# for index, item in enumerate(grocery, 1):
#     print(f"{index}. {item}")


# for i in range(start, stop, step):
#     print(i)


# for i in range(10, 0, -1):
#     print(i)


# slice #   seq = [start, stop, step]
# seq [1:4]
# 0, 1, 2, 3, 4 : 1 2 3 are included

# rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# print(rainbow[::2])

# my_name = "Anthony"
# print(my_name[0:3])


# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(len(nums))

# print(max(nums))

# print(min(nums))

# my_string = "treehouse"
# print(len(my_string))
# print(max(my_string))
# print(min(my_string))

# mixed = "treehouse2019"
# print(max(mixed))
# print(min(mixed))


# docs = "Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in).  Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance)."

# if "of" in docs:
#     print("Of is not here!")
# else:
#     print("Of is here!")

# print(docs.count("tuple"))
# print(docs.index("tuple"))


# teachers = ["Alena", "Ashley", "Nicole", "Treasure"]

# print(teachers.index("Nicole"))


# object1 = (1, 2, 3, 4, 5)
# object2 = (6, 7, 8, 9, 10)

# object1 = object1 + object2
# print(object1)


# str = "python "

# print(str*5)


#-----------------------------------------------------------------------#
# Introducing Dictionaries in Python #
#-----------------------------------------------------------------------#

# {key:value}

# course = {"teacher":"Ashley", "title":"Introducing Dictionaries", "Level":"Beginner"}

# print(course["teacher"])
# course.keys()
# course.values()

# sorted(course.keys())
# sorted(course.values())

# for item in course:
#     print(course[item])

# for item in course.items():
#     print(item)

# for key, value in course.items():
#     print(key)
#     print(value)

# def print_teacher(name, job, topic):
#     print(name)
#     print(job)
#     print(topic)

# def print_teacher(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')

# print_teacher(name="Ashley", job="Instructor", topic="Python", second_topic="Javascript")


#-----------------------------------------------------------------------#
# Understanding Dunder Main (__main__) #
#-----------------------------------------------------------------------#

# __method name__ is a double under or "dunder"

# def print_hello():
#     print("Hello from app.")

# print(__name__)

# if __name__ == '__main__':
#     print_hello()


#-----------------------------------------------------------------------#
# Object-Oriented Python #
#-----------------------------------------------------------------------#

# class is int, str, list

class Warrior:
    melee = True

