import dataclasses
import pytest
import testlib

from missing_number import find_missing_number


@dataclasses.dataclass
class Case:
    string: str
    number: int

    def __str__(self) -> str:
        return "is_prime_{}".format(self.string)


TEST_CASES = [
    Case(string='123456789', number=0),
    Case(string='237658904', number=1),
    Case(string='890712356', number=4),
    Case(string='654321890', number=7),
]


###################
# Structure asserts
###################


def test_docs() -> None:
    assert testlib.is_function_docstring_exists(find_missing_number)


###################
# Tests
###################


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_find_missing_number(t: Case) -> None:
    st = t.string
    assert find_missing_number(t.string) == t.number

    assert st == t.string, "You shouldn't change input"
