import pytest
from problem3_func import convert_units 

def test_convert_units():
	assert convert_units(4, "pound","kilogram") == 1.8
	assert convert_units(2, "mile", "kilometer") == 3.22
	assert convert_units(32, "fahrenheit", "celsius") == 0
	assert convert_units(2, "gallon", "liter") == 7.58


