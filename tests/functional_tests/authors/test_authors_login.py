import pytest

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    @pytest.mark.on_focus
    def test_the_test(self):
        assert 1 == 1
