from src.hello_world import say_hello


def test_hello_world():
    assert say_hello() == "Hello world!"
