# import pytest
# from problem3_func import convert_units 
# 
# def test_convert_units():
# 	assert convert_units(4, "pound","kilogram") == 1.81
# 	assert convert_units(2, "mile", "kilometer") == 3.22
# 	assert convert_units(32, "fahrenheit", "celsius") == 0
# 	assert convert_units(2, "gallon", "liter") == 7.58

# Updated version: Separated tests in multiple functions. Used parametrization to minimize code. Tests have higher coverage.

import pytest
from problem3_func import convert_units 
from pytest import approx

@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
	(4, "pound", "kilogram", 1.81),
])
def test_convert_weight(value, from_unit, to_unit, expected):
	assert convert_units(value, from_unit, to_unit) == approx(expected, 0.01)

@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
	(2, "mile", "kilometer", 3.22),
])
def test_convert_distance(value, from_unit, to_unit, expected):
	assert convert_units(value, from_unit, to_unit) == approx(expected, 0.01)

@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
	(32, "fahrenheit", "celsius", 0),
])
def test_convert_temperature(value, from_unit, to_unit, expected):
	assert convert_units(value, from_unit, to_unit) == approx(expected, 0.01)

@pytest.mark.parametrize("value, from_unit, to_unit, expected", [
	(2, "gallon", "liter", 7.58),
])
def test_convert_volume(value, from_unit, to_unit, expected):
	assert convert_units(value, from_unit, to_unit) == approx(expected, 0.01)

