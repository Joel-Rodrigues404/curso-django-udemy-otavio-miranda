"""
Testes da função de paginação
"""

from unittest import TestCase
from utils.recipes.pagination import make_pagination_range


class PaginationTest(TestCase):
    """Testes de paginação"""

    def test_make_pagination_range_returns_a_pagination_range(self):
        """Testa se os elementos estão sendo exibidos corretamente"""
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        """Testa se os elementos estão sendo exibidos corretamente"""
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=2
        )["pagination"]
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=3
        )["pagination"]
        self.assertEqual([2, 3, 4, 5], pagination)

    def test_make_sure_middle_ranges_are_correct(self):
        """Testa se os elementos estão sendo exibidos corretamente"""
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=10
        )["pagination"]
        self.assertEqual([9, 10, 11, 12], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=12
        )["pagination"]
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        """Testa se a lista de numeros e interrompida quando chega a seu limite"""
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=18
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=19
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=29
        )["pagination"]
        self.assertEqual([17, 18, 19, 20], pagination)
