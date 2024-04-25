import math

def make_pagination_range(page_range, qty_pages, current_page):
    middle_range = math.ceil(qty_pages / 2)
    start_range = 0
    stop_range = qty_pages
    return page_range[start_range, stop_range]
