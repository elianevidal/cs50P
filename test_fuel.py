from fuel2 import convert, gauge
from pytest import raises

assert convert("1/2") == 50 and gauge(50) == '50%'
assert convert("1/1") == 100 and gauge(100) == 'F'
assert convert("1/3") == 33 and gauge(33) == '33%'
assert convert("1/100") == 1 and gauge(1) == 'E'

with raises(ZeroDivisionError):
    convert("1/0")
    convert("0/0")

with raises(ValueError):
    convert("cat/1")
    convert("2/1")
    convert("1.0/6")