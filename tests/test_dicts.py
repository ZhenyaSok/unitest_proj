from utils import dicts

data = {"vcs": "mercurial"}


def test_get_val():
    assert dicts.get_val({}, None)
    assert dicts.get_val({}, "vcs", "bazaar")
    assert dicts.get_val(data, "vcs")
    assert dicts.get_val(data, "vcs", "mercurial")

