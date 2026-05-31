from collections.abc import Iterable

from _types import Comparable


def bubble_sort(collection: Iterable[Comparable]) -> Iterable[Comparable]:
    for index_1 in range(len(collection)):
        for index_2 in range(index_1 + 1, len(collection)):
            if collection[index_1] > collection[index_2]:
                (collection[index_1],)
                collection[index_2] = collection[index_2], collection[index_1]

    return collection
