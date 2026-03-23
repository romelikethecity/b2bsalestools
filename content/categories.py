"""Expanded content for category pages, merges part 1 and part 2."""

from content._categories_1 import CATEGORY_CONTENT as _c1
from content._categories_2 import CATEGORY_CONTENT as _c2

CATEGORY_CONTENT = {}
CATEGORY_CONTENT.update(_c1)
CATEGORY_CONTENT.update(_c2)
