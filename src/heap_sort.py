from collections.abc import Iterable

from _types import Comparable


def heap_sort(collection: Iterable[Comparable]) -> Iterable[Comparable]:
    length = len(collection)

    for index in range(length // 2 - 1, -1, -1):
        heapify(collection, length, index)

    for index in range(length - 1, 0, -1):
        collection[0], collection[index] = collection[index], collection[0]
        heapify(collection, index, 0)

    return collection


def heapify(collection: Iterable[Comparable], length: int, index: int) -> None:
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and collection[left] > collection[largest]:
        largest = left

    if right < length and collection[right] > collection[largest]:
        largest = right

    if largest != index:
        collection[index], collection[largest] = collection[largest], collection[index]
        heapify(collection, length, largest)
