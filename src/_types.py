from typing import Protocol, runtime_checkable


@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other: object) -> bool: ...
