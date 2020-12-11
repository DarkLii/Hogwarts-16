import pytest


class TestHogwarts:
    params = [
        [3, 5, 8],
        [-1, -2, -3],
        [1000, 2000, 3000],
    ]
    ids = ["int", "minus", "bigint"]

    @pytest.mark.parametrize("a,b,expected", params, ids=ids)
    def test_one(self, a, b, expected):
        assert a + b == expected

    # Õý½»
    @pytest.mark.parametrize("a", [1, 2])
    @pytest.mark.parametrize("b", [3, 4])
    def test_two(self, a, b):
        print(f"a={a},b={b}")
