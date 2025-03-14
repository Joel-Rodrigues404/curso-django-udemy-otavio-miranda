from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import RecipeBaseFunctionalTest
from unittest.mock import patch
import pytest


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):

    # @pytest.mark.functional_test
    @patch("recipes.views.PER_PAGE", new=2)
    def test_recipe_home_page_without_recipes_not_found_message(self):
        """Deve mostrar uma mensagem de erro quando não houver receitas"""

        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn("No Recipes found here :)", body.text)

    @patch("recipes.views.PER_PAGE", new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        """Deve permitir o usuário buscar por receitas"""
        recipes = self.make_recipe_in_batch()

        title_needed = "Needed title"
        recipes[0].title = title_needed
        recipes[0].save()

        # Usuario abre a pagina
        self.browser.get(self.live_server_url)

        # Ve um campo de busca com o testo "Search for a recipe..."
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe..."]'
        )

        # clica neste input e digita o texto de busca
        # para encontrar a receita com o titulo desejado

        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        # Aguarda a receita aparecer na página antes de continuar
        wait = WebDriverWait(self.browser, 1)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, 'main-content-list'), title_needed
            )
        )

        # o usuario ve o que estava procurando na pagina
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME, 'main-content-list').text
        )

    @patch("recipes.views.PER_PAGE", new=2)
    def test_recipe_home_page_pagination(self):
        """Deve permitir o usuário navegar entre as páginas de receitas"""
        self.make_recipe_in_batch()

        # Usuario abre a pagina
        self.browser.get(self.live_server_url)

        # ve que tem uma paginação e clica na pagina 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'
        )
        page2.click()

        # ve que tem mais 2 receitas na pagina 2
        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')),
            2
        )
