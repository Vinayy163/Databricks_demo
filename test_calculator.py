from calculator import add,multiply,substract

def test_add():
  assert add(2,3)==5

def test_multiply():
  assert multiply(3,4)==12

def test_substract():
  assert substract(5,2)==3