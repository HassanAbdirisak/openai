import pytest
from whisper.utils import str2bool

def test_str2bool_case_insensitive():
    assert str2bool('True') is True
    assert str2bool('true') is True
    assert str2bool('FALSE') is False
    assert str2bool('0') is False
    assert str2bool('1') is True
    assert str2bool('Yes') is True
    assert str2bool('n') is False

    with pytest.raises(ValueError):
        str2bool('maybe')
