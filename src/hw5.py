
# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message:
# "Undefined instruction for color: <light>"
# where <light> is the value of the parameter light.
# comment

def car_at_light(light):
    if light == "red":
        return "stop"

    elif light == "green":
        return "go"

    elif light == "yellow":
        return "wait"

    else:
        raise Exception("Undefined instruction for color: " + str(light))

car_at_light("red")


# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type,
# it returns None.
# If there is any other reason why it fails show the problem
#

def safe_subtract(num1,num2):
    try:
        return num2-num1
    except TypeError:
        return None

safe_subtract(1, 5)

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl
from datetime import datetime
person1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
person2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}

def retrieve_age_eafp(dict):
    try:
        age = datetime.now().year - dict['birth']
        return age
    except KeyError as e:
        print(e, 'Keys for calculating age are missing')
        raise

def retrieve_age_lbyl(person):
    if 'birth' in person:
        return datetime.now().year-person['birth']
    else:
        raise KeyError('birth not defined')

# 4)
# Imagine you have a file named data.csv.
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact
# that it might not exist.
#

import pandas as pd

def read_data(file):
    try:
        return pd.read_csv(file)
    except FileNotFoundError:
        raise

read_data('sample_diabetes_mellitus_data.csv')

# 5) Squash some bugs!
# Find the possible logical errors (bugs)
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

total_double_sum

## The error here is that total_double_sum adds the elements in the list, not the double elements.
## That is, we are doubling the numbers but summing over the oriignals, rather than the doubled.
## To correct it, we would need:
total_double_sum2 = 0
for elem in [10, 5, 2]:
    double2 = elem * 2
    total_double_sum2 += double2

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

## The error here is that strings is concatenating the individual elements twice, rather than looping through each element.
## To correct it, we would need to add each element to strings, although nota that this would leave us with a string that begins with "_".
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = strings+'_'+string

### (c) Careful!
j=10
while j > 0:
   # j += 1
   j-=1

## The error here is that our while loop continues forever, as we have not specified when it should break.
## To correct it, we would need to add a break once j reaches a specified value, such as 100.

j=10
while j > 0:
   j += 1
   if j == 100:
    break

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

## The error here is that we specify productory = 0. That means in the for loop we multiply the element by 0, which results in... 0!
## To correct it, we could add a step in the for loop in which define productory to be equal to the element, and then multiply them.

productory = 0
for elem in [1, 5, 25]:
    productory = elem
    productory *= productory

################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

list1 = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
def count_simba(x):
    return sum(map(lambda y : y.split().count("Simba") , x))

count_simba(list1)

# 7)
# Create a function called "get_day_month_year" that takes
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its
# day, month, and year.
from datetime import datetime

datelist = ['02-09-1997','17-11-2022','10-04-1968']
datelist = [datetime.strptime(date, '%d-%m-%Y') for date in datelist]

def get_day_month_year(datelist):
    import pandas as pd
    year, month, day = [], [], []
    for i in datelist:
        year.append(i.year), month.append(i.month), day.append(i.day)
    df = pd.DataFrame(list(zip(day, month, year)),
               columns =['Day', 'Month', 'Year'])
    return df

get_day_month_year(datelist)


# 8)
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
coordinates = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

def compute_distance(list):
    dist_list = []
    for element in list:
        x_dist = element[0][0] - element[1][0]
        y_dist = element[0][1] - element[1][1]
        dist = (x_dist**2 + y_dist**2)**0.5
        dist_list.append(dist)
    return dist_list

compute_distance(coordinates)

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1].
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]]
# the result should be 13

list_1 = [[2], 3, [[1,2],5]]

def sum_general_int_list(my_list):
    sum = 0
    for i in my_list:
        if isinstance(i, list):
            sum += sum_general_int_list(i)
        else:
            sum += i
    return sum

sum_general_int_list(list_1)
