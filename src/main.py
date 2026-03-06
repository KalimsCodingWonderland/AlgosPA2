import sys
from collections import deque, OrderedDict

def fifo_cache(k: int, requests: list[int]) -> int:
    cache: set[int] = set()
    order: deque[int] = deque()
    misses = 0

    for page in requests:
        if page in cache:
            continue

        misses += 1
        if len(cache) == k:
            evict = order.popleft()
            cache.remove(evict)
        cache.add(page)
        order.append(page)

    return misses

def lru_cache(k: int, requests: list[int]) -> int:
    cache = OrderedDict()
    misses = 0

    for page in requests:
        if page in cache:
            cache.move_to_end(page)
        else:
            misses += 1

            if len(cache) == k:
                cache.popitem(last=False)

            cache[page] = None

    return misses



def _next_occurrence(page: int, after: int, requests: list[int], m: int) -> int:
    for j in range(after + 1, m):
        if requests[j] == page:
            return j
    return m
