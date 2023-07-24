import pytest

# Fixture for the multiplication table
@pytest.fixture
def multi_table(): # From PE2
	multi_table = [["X"] + [str(i) for i in range(1, 13)]]
	for i in range(1, 13):
		row = [str(i)]
		for j in range(1, 13):
			row.append(str(i * j))
		multi_table.append(row)
	return multi_table

# Two basic tests
@pytest.mark.basic
def test_dimensions(multi_table):
	assert len(multi_table) == 13
	for row in multi_table:
		assert len(row) == 13

@pytest.mark.basic
def test_headers(multi_table):
	for i in range(1, 13):
		assert multi_table[0][i] == str(i)
		assert multi_table[i][0] == str(i)

# Test expected to fail
@pytest.mark.xfail
def test_fail(multi_table):
	assert multi_table[0][0] == "1"

# Test for IndexError
def test_index_error(multi_table):
	with pytest.raises(IndexError):
		_ = multi_table[13]

# Parametrized test
@pytest.mark.parametrize(
	"input,expected", [((1, 1), '1'), ((2, 2), '4'), ((3, 3), '9'), ((4, 4), '16')]
)
def test_multiplication_results(multi_table, input, expected):
	i, j = input
	assert multi_table[i][j] == expected
