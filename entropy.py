"""Shannon entropy calculation."""

import math
from collections import Counter
from collections.abc import Sequence
from typing import Hashable


def shannon_entropy(data: Sequence[Hashable]) -> float:
    """Return the Shannon entropy of the empirical distribution of `data`, in bits."""
    n = len(data)
    if n == 0:
        return 0.0
    # abs() avoids returning -0.0 for single-valued data.
    return abs(-sum((c / n) * math.log2(c / n) for c in Counter(data).values()))
