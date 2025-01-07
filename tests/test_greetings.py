from ..greetings import greet
def test_greet_function_prints_hello_world():
    assert greet() == 'Hello World!'