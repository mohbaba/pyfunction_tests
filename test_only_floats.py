from only_floats import *

def test_only_floats():

	assert only_floats(1,2) == 0
	assert only_floats(1,2.5) == 1
	assert only_floats(1.3,2.5) == 2