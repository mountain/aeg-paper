from dataclasses import dataclass
from typing import Any, cast
from typing_extensions import TypeVar, runtime_checkable, Protocol

T = TypeVar("T")
MonoidT = TypeVar("MonoidT", bound="FiniteMonoid")
MonoidalT = TypeVar("MonoidalT", bound="Monoidal")


@runtime_checkable
class FiniteMonoid(Protocol):
    """Structural interface for values obeying monoid-style composition."""

    @classmethod
    def identity(cls: type[MonoidT]) -> MonoidT:
        ...

    def combine(self: MonoidT, other: MonoidT) -> MonoidT:
        ...

    def __iter__(self):
        return self.combine(self)


@dataclass(frozen=True, slots=True)
class Monoidal:
    """A small additive monoid wrapper.

    Subclasses may override `identity_value` and `combine_values` to model a
    different monoid while preserving the same laws-oriented interface.
    """

    value: Any

    @classmethod
    def identity_value(cls) -> Any:
        return 0

    @classmethod
    def identity(cls: type[MonoidalT]) -> MonoidalT:
        return cls(cls.identity_value())

    @classmethod
    def _zero_(cls: type[MonoidalT]) -> MonoidalT:
        """Backward-compatible alias for the identity element."""
        return cls.identity()

    @classmethod
    def combine_values(cls, left: Any, right: Any) -> Any:
        return left + right

    def combine(self: MonoidalT, other: MonoidalT) -> MonoidalT:
        if type(self) is not type(other):
            return NotImplemented
        return type(self)(self.combine_values(self.value, other.value))

    def __add__(self: MonoidalT, other: MonoidalT) -> MonoidalT:
        return self.combine(other)

    def __radd__(self: MonoidalT, other: object) -> MonoidalT:
        if other == 0:
            return self
        if type(other) is type(self):
            return cast(MonoidalT, other).combine(self)
        return NotImplemented

    def satisfies_identity(self) -> bool:
        identity = type(self).identity()
        return self.combine(identity) == self and identity.combine(self) == self

    def is_associative_with(self: MonoidalT, middle: MonoidalT, right: MonoidalT) -> bool:
        return self.combine(middle).combine(right) == self.combine(middle.combine(right))
