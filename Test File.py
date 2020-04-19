# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print((23+32+64)/3)

# Fill this in with an expression that calculates how many tiles are needed.
print((63+35)//5)
# Fill this in with an expression that calculates how many tiles will be left over.
print((17*6)-98)

#Which of these lines of Python code are well formatted? How would you improve the readability of the codes that don't use good formatting? (Choose all that apply)
print((17-6)%(5+2))
print(4/2- 7*7)

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)

>>> crs_per_rab = carrots/rabbits
>>> print(crs_per_rab)
2.0

#In the fishy situation below, some of the quantities are of type int and some are of type float. Check all the ones that should be of type float.
#Answer: Length of fish you caught in meters and length of time it took in hours

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5
san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area
# Write code that prints True if San Francisco is denser than Rio, and False otherwise
is_san = san_francisco_pop_density>rio_de_janeiro_pop_density
print(is_san)

#Why do you think Python uses == for checking equality rather than =?
# Answer: Because = is used to assign variables

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."

# 3415(and tropical_fruit_count is a string)

print (username + " accessed the site " + url + " at " + timestamp + ".")

name_length = len(given_name) + len(middle_names) + len(family_name) + 2

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)
print("This week's total sales: " + weekly_sales)

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# use list indexing to determine the number of days in month
num_days = 31
print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
q3 = eclipse_dates[7:9]
print(q3)


population = {'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}


elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")
verse_list = verse.split()
print(verse_list, '\n')
verse_set = set(verse_list)
print(verse_set, '\n')
num_unique = len(verse_set)
print(num_unique)

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')
num_keys = len(verse_dict)
print(num_keys)
contains_breathe = "breathe" in verse_dict
print(contains_breathe)
sorted_keys = sorted(verse_dict.keys())
print(sorted_keys[0])
print(sorted_keys[-1])

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)

answer = 47
guess = 53

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer
    result = "Nice!  Your guess matched the answer!"

print(result)

points = 174  # use this as input for your submission
prize = None
# establish the default prize value to None


# use the points value to assign prizes to the correct prize names
prize = Wafer-thin mint
if prize == None:
    result = ("Oh dear, no prize this time.")
elif prize == wafer-thin mint:
    result = ("Congratulations! You won a wafer-thin mint!".format(prize))

# use the truth value of prize to assign result to the correct prize
print(result)

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

line = line[:1].replace(';',':')+line[:1]
# write your for loop here
for name in names:
    usernames.append(names)

print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1
print(count)

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
   if object in fruits:
       result += count
print("There are {} fruits in the basket.".format(result))

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']


for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count
print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))



number = 6
product = 1
current = 1

while  current <= number:
    product *= current
    current += 1

print(product)



number = 6
product = 1
for num in range(2, number + 1):
    product *= num
print(product)

start_num =1
end_num = 31
count_by = 3

break_num = []

while sum(break_num) <= end_num:
    break_num.append(end_num)
#   check against end_num
print(break_num)

start_num = 3
end_num = 30
count_by = 3
break_num = []

if end_num >= start_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    result = break_num

while break_num <= end_num:
    break_num.append(end_num)
# write a while loop that uses break_num as the ongoing number to
#   check against end_num

print(result)

limit = 40
nearest_square = 36
largest_square = []

while largest_square < limit:
    largest_square.append(nearest_square)
# write your while loop here

print(nearest_square)

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
characters = int(140)
news_ticker = ""
while news_ticker <= characters:
    Break
    news_ticker.append(headlines + '')
print(news_ticker)

check_prime = [26, 39, 51, 53, 57, 79, 85]
if i in check_prime is prime:
    print(i , "is a prime number")
elif i in check_prime is not prime:
    print(i, "is not prime")

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
for item in zip(labels, x_coord, y_coord, z_coord):
    item.append(points)

for point in points:
    print(point)


cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = dict(zip(cast_names, cast_heights))
print(cast)

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)
print(names)
print(heights)

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])
print(cast)

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.lower() for name in names]
print(first_names)

multiples_3 = [x*3 for x in range (20)]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [name for name, score in scores.items() if score >= 65]
print(passed)

nom_count_dict = {}
for year, list_dir in nominated.items():
    for director in list_dir:
        if director not in nom_count_dict:
            nom_count_dict[director] = 1
        else:
            nom_count_dict[director] += 1

in_count_dict = {}
for year, winnerlist in winners.items():
    for winner in winnerlist:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1
highest_count = 0
most_win_director = []

for key, value in win_count_dict.items():
    if value > highest_count:
        highest_count = value
        most_win_director.clear()
        most_win_director.append(key)
    elif value == highest_count:
        most_win_director.append(key)
    else:
        continue


def population_density(population, land_area):
    return population/land_area
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))
test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

def readable_timedelta(days):
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)
print(readable_timedelta(10))

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

mean = lambda num_list: sum(num_list)/ len(num_list)

averages = list(map(mean, numbers))
print(averages)

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short = lambda name: len(name) < 10
short_cities = list(filter(is_short, cities))
print(short_cities)

def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)


def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)
    return cast_list
cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

user_list = []
list_sum = 0
for i in range(10):
    userInput = int(input("Enter any number: "))
    try:
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError:
        print("Incorrect value. That's not an int!")
print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))

math.exp(x):
    x=3
    return(e**x)
print(math.exp(x))

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


