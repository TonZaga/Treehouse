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

name = input("Please enter your name: ")
number = input("Please enter a number: ")
number = int(number)
    
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

print("Hey, {}!\nYour number is {}".format(name, number))

if is_fizz and is_buzz:
    print("{} is a FizzBuzz number.".format(number))
elif is_fizz:
    print("{} is a Fizz number.".format(number))
elif is_buzz:
    print("{} is a Buzz number.".format(number))
else:
    print("{} is neither a fizzy or a buzzy number".format(number))