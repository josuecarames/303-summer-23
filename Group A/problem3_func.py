def convert_units(amount, us_unit, metric_unit):
	if not isinstance(amount, (float, int)) or amount < 0:
		raise Exception("Amount must be a nonnegative number of type float or integer.")
	
	if not isinstance(us_unit, str) or not isinstance(metric_unit, str):
		raise Exception("US unit and metric unit must be strings.")
	
	if us_unit == metric_unit:
		return amount
	
	conversion_rates = {
		("pound", "kilogram"): 0.453592,
		("mile", "kilometer"): 1.60934,
		("fahrenheit", "celsius"): lambda f: 5/9*(f-32),
		("gallon", "liter"): 3.79
	}
	
	try:
		conversion = conversion_rates[(us_unit, metric_unit)]
		return conversion(amount) if callable(conversion) else conversion * amount
	except KeyError:
		raise Exception(f"Invalid conversion requested from {us_unit} to {metric_unit}.")
