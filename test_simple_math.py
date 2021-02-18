#test simple_math.py
import simple_math as sm

def test_add():
	assert sm.simple_add(1, 1) == 2

def test_sub():
	assert sm.simple_sub(1, 1) == 0

def test_mult():
	assert sm.simple_mult(2, 4) == 8

def test_div():
	assert sm.simple_div(8, 2) == 4

def test_poly_first():
	assert sm.poly_first(2, -4, 2) == 0

def test_poly_second():
	assert sm.poly_second(-2, 4, 4, 1) == 0
