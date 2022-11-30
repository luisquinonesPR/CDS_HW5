import unittest
import pytest
from pandas.testing import assert_frame_equal
from src.hw5 import *
import pandas as pd
from datetime import datetime

# TESTS

class Test_HW5(unittest.TestCase):

    # Q1 Tests
    def test_car_at_light_else(self):
        light = "blue"
        with pytest.raises(Exception, match = "Undefined instruction for color: " + str(light)):
            car_at_light(light)

    def test_car_at_light_red(self):
        assert car_at_light("red") == "stop"

    def test_car_at_light_green(self):
        assert car_at_light("green") == "go"

    def test_car_at_light_yellow(self):
        assert car_at_light("yellow") == "wait"

    # Q2 Tests

    def test_safe_subtract_valid(self):
        assert safe_subtract(1,5) == 4

    def test_safe_subtract_invalid(self):
        with pytest.raises(TypeError):
            safe_subtract(1)

    # Q3 Tests

    def test_retrieve_age_eafp(self):
        output=retrieve_age_eafp({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
        expected_output= 35
        self.assertEqual(output,expected_output)
        with self.assertRaises(KeyError):
            retrieve_age_eafp({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})
    def test_retrieve_age_lbyl(self):
        output=retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
        expected_output= 35
        self.assertEqual(output,expected_output)
        with self.assertRaises(KeyError):
            retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})

    # Q4 Tests

    def test_read_data(self):
        expected_output = pd.read_csv("sample_diabetes_mellitus_data.csv")
        output = read_data("sample_diabetes_mellitus_data.csv")
        assert_frame_equal(output, expected_output)
        with self.assertRaises(FileNotFoundError):
            read_data('whatever.csv')


   ## Q6 Tests
    def test_count_simba_valid(self):
        assert count_simba(["Simba and Nala are lions.", "I laugh in the face of danger.",
        "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]) == 3

    ## Q7 Tests

    def test_get_day_month_year_valid(self):
        datelist = ['02-09-1997','17-11-2022','10-04-1968']
        datelist = [datetime.strptime(date, '%d-%m-%Y') for date in datelist]
        data = [[2,9,1997],[17,11,2022],[10,4,1968]]
        expected_output = pd.DataFrame(data, columns = ['Day', 'Month', 'Year'])
        output = get_day_month_year(datelist)
        assert_frame_equal(output, expected_output)


    ## Q8 Tests
    def test_compute_distance(self):
        assert compute_distance([((0,0), (10, 0)), ((10, 10),(14, 13))]) == [10,5]

    ## Q9 Tests

    def test_sum_general_int_list(self):
        assert sum_general_int_list([[1], 2, [[3,4],5]]) == 15
