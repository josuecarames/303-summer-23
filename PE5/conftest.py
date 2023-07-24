import pytest
import time

@pytest.fixture(autouse=True)
def timer():
	start = time.time()
	yield
	end = time.time()
	print("\nTest duration: ", end - start, "seconds")
