a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def find_gcd(a, b):
	# Check if integers are positive
	if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0: 
		raise Exception("Error, the input value must be a positive integer")
	
	if a < b:
		a, b = b, a
	while b:
		r = a%b
		if r == 0:
			return b
		a, b = b, r
	return b

print(find_gcd(a, b))