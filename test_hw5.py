## Q1 Tests
from hw5 import car_at_light

def test_car_at_light_else():
    light = "blue"
    with pytest.raises(Exception, match = "Undefined instruction for color: " + str(light)):
        car_at_light(light)

def test_car_at_light_red():
    assert car_at_light("red") == "stop"

def test_car_at_light_green():
    assert car_at_light("green") == "go"

def test_car_at_light_yellow():
    assert car_at_light("yellow") == "wait"

## Q2 Tests
from hw5 import safe_subtract

def test_safe_subtract_valid():
    assert safe_subtract(1,5) == 4

def test_safe_subtract_invalid():
    with pytest.raises(TypeError):
        safe_subtract(1)

## Q3 Tests
from hw5 import retrieve_age_eafp, retrieve_age_lbyl

def test_retrieve_age_eafp_valid():
    my_dict_valid = {'birth': 1987}
    assert retrieve_age_eafp(my_dict_valid) == 1987

def test_retrieve_age_eafp_invalid():
    my_dict_invalid = {'gender':'female'}
    with pytest.raises(KeyError, match = "Oh dear! Looks like you didn't provide that information!"):
        retrieve_age_eafp(my_dict_invalid)

def test_retrieve_age_lbyl_valid():
    my_dict_valid = {'birth': 1987}
    assert retrieve_age_lbyl(my_dict_valid) == 1987

def test_retrieve_age_lbyl_invalid():
    my_dict_invalid = {'gender':'female'}
    with pytest.raises(KeyError, match = "Oh dear! Looks like you didn't provide that information!"):
        retrieve_age_lbyl(my_dict_invalid)

######## Should we be testing for things we know our function doesn't cover?
######## For example, if the year is passed as a string, it will raise a TypeError rather than KeyError, so our test will only pass bc we are not considering this
######## And we only did not consider this because he said to create a function that would handle a specific example which did not include string...

## Q4 Tests
from hw5 import read_data


##### Unclear how to assert equivalence of these dataframes. Compare to pd.read_csv? The same error would occur if file not found...

## Q5 Tests

##### No functions were created for this question

## Q6 Tests
from hw5 import count_simba

def test_count_simba_valid():
    assert count_simba(["Simba and Nala are lions.", "I laugh in the face of danger.", 
    "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]) == 3

## Q7 Tests
from hw5 import get_day_month_year
from datetime import datetime

def test_get_day_month_year_valid():
    datelist = ['02-09-1997','17-11-2022','10-04-1968']
    datelist = [datetime.strptime(date, '%d-%m-%Y') for date in datelist]
    data = [[2,9,1997],[17,11,2022],[10,4,1968]]
    assert get_day_month_year(datelist) == pd.DataFrame(data, columns = ['Day', 'Month', 'Year'])

##### Is this how you do this??? I found other ways but only using unittest and pandas.testing

## Q8 Tests
from hw5 import dist

def test_dist_valid():
    assert dist([((0,0), (10, 0)), ((10, 10),(14, 13))]) == [10,5]

## Q9 Tests
from hw5 import sum_general_int_list

def test_sum_general_int_list():
    assert sum_general_int_list([[1], 2, [[3,4],5]]) == 15
