from hello import hello_world


def test_hello_world():
    """
    The function tests whether the output of the hello_world function with the input "John" is equal to
    the string "Hello, John".
    """
    assert "Hello, John" == hello_world("John")
