from string_tools import reverse, to_upper

def test_reverse():
    assert reverse("abc") == "cba"

def test_upper():
    assert to_upper("abc") == "ABC"
