import pytest
from lesson_04.string_utilits import StringUtils 

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize ("input_str, expected", [
    ("   hi", "hi"),
    ("        sugar and tea", "sugar and tea"),
    ("Phone", " Phone"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ('',''),
    ('test   ', 'test   '),
    ('santa', 'santa'),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected",[
    ('symbol', 's', True),
    ('tree', 'd', False),
    ('New Year', 'n', True)
])
def test_contains_positive(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected

@pytest.mark.xfail(reason= "Негативные тесты")
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected",[
    ('', 'm', True),
    ('......', 'd', True),
    ('    ', 'l', True)
])
def test_contains_negative(input_str, input_sym, expected):
    assert string_utils.contains(input_str, input_sym) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_sym, expected", [
    ('frozen', 'n', 'froze'),
    ('snow', 'd', 'snow'),
    ('lucky boy', ' ', 'luckyboy')
])
def test_delete_symbol_positive(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected

@pytest.mark.xfail(reason= "Негативные тесты")
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_sym, expected",[
    ('party', 'p', 'party'),
    ('321456', '2', '21456'),
    ('Yyear', 'y', 'year')
])
def test_delete_symbol_negative(input_str, input_sym, expected):
    assert string_utils.delete_symbol(input_str, input_sym) == expected