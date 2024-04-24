from unittest import skip
from recipes.tests.test_recipe_base import RecipeTestBase


class OthersTest(RecipeTestBase):
    """Faço testes de testes"""

    # -=--=-=--=-=--=-=--= Others -=--=-=--=-=--=-=--=-=--=-=--=
    @skip("WIP")
    def test_test_for_skip(self):
        """Teste para skipar"""
        assert 1 == 1

        # Se Eu ainda tiver que escrever mais algum codigo
        self.fail("Tem que fazer tal tal tal ...")
