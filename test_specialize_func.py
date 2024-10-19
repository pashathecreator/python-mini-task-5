import pytest
from main import Vector2D, dot_product, sum, multiply, some_calculation, specialize

def test_specialize_sum():
    specialized_sum = specialize(sum, 2)
    assert specialized_sum(3) == 5

def test_specialize_multiply():
    specialized_multiply = specialize(multiply, 2, 3)
    assert specialized_multiply(4) == 24

def test_specialize_dot_product():
    v1 = Vector2D(2, 3)
    specialized_dot_product = specialize(dot_product, v1)
    v2 = Vector2D(4, 5)
    assert specialized_dot_product(v2) == 23

def test_specialize_with_kwargs():
    specialized_calc = specialize(some_calculation, 1, 2, 3)
    assert specialized_calc(d=10, e=2) == 58

def test_specialize_with_default_kwargs():
    specialized_calc = specialize(some_calculation, 1, 2)
    assert specialized_calc(3) == 19

def test_specialize_no_args():
    specialized_multiply = specialize(multiply, 2)
    assert specialized_multiply(3, 4) == 24
    
if __name__ == "__main__":
    pytest.main()