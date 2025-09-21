from src.task2 import use_int, use_float, use_str, use_bool

def test_int_type_and_value():
    v = use_int()
    assert isinstance(v, int)
    assert v == 42

def test_float_type_and_value():
    v = use_float()
    assert isinstance(v, float)
    assert v == 5.0

def test_str_type_and_value():
    v = use_str()
    assert isinstance(v, str)
    assert v == "Hello, World!"

def test_bool_type_and_value():
    v = use_bool()
    assert isinstance(v, bool)
    assert v is True
