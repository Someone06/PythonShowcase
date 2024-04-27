from abc import ABC, abstractmethod


class Base:
    def __init__(self, name: str) -> None:
        self._name = name

    def hello(self) -> None:
        print(f"Hello from {self._name}")


class Derived(Base):
    def __init__(self) -> None:
        super().__init__("Base")

    def hello(self) -> None:
        super().hello()
        print("Hello from Derived")


class AbstractBase(ABC):
    @abstractmethod
    def test(self) -> None:
        ...

class Concrete(AbstractBase):
    def test(self) -> None:
        print("Implemented test")


def main() -> None:
    t = Concrete()
    t.test()


if __name__ == "__main__":
    main()