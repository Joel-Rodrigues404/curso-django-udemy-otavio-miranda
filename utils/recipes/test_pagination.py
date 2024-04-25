from unittest import TestCase
from utils.recipes.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1
        )
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        # Current page = 1 - qty Page = 2 - middel page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1
        )
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 2 - qty Page = 2 - middel page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=2
        )
        self.assertEqual([1, 2, 3, 4], pagination)

        # Current page = 3 - qty Page = 2 - middel page = 2
        pagination = make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=3
        )
        self.assertEqual([2, 3, 4, 5], pagination)
