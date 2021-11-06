def multiple(num1: int, num2: int) -> int:
    return num1 * num2


def test_multiple():
    result = multiple(3, 5)
    assert result == 15
    