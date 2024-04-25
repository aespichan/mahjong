import pytest
from mahjong import Mahjong

class TestMahjong:
    @pytest.mark.parametrize(
        "input,expected", 
        [
            ("1,1,1,2,3,2,3,4,3,3,3,4,4,4", True), 
            ("1,1,6,2,3,2,3,4,3,3,3,4,4,4", False),
        ]
    )
    def test_is_winning_hand(self, input, expected):
        assert Mahjong.is_winning_hand(input) == expected