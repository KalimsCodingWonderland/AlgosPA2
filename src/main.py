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

def optff_cache(k: int, requests: list[int]) -> int:
    cache = set()
    misses = 0
    m = len(requests)

    for i in range(m):
        page = requests[i]

        if page in cache:
            continue

        misses += 1

        if len(cache) == k:
            victim = None
            farthest_next_use = -1

            for cached_page in cache:
                next_use = _next_occurrence(cached_page, i, requests, m)

                if next_use > farthest_next_use:
                    farthest_next_use = next_use
                    victim = cached_page

            cache.remove(victim)

        cache.add(page)

    return misses

def _next_occurrence(page: int, after: int, requests: list[int], m: int) -> int:
    for j in range(after + 1, m):
        if requests[j] == page:
            return j
    return m
