import pytest
from stack import Stack

@pytest.fixture
def stack():
    return Stack()

def test_push(stack):
    stack.push(1)
    stack.push(2)
    assert stack.count == 2

def test_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    data = stack.pop()
    assert data == 3
    assert stack.count == 2



