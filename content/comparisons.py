"""Expanded content for comparison pages, merges part 1 and part 2."""

from content._comparisons_1 import COMPARISON_CONTENT as _c1
from content._comparisons_2 import COMPARISON_CONTENT as _c2

COMPARISON_CONTENT = {}
COMPARISON_CONTENT.update(_c1)
COMPARISON_CONTENT.update(_c2)
