# Notes:
# - Line breaks and indentation between brackets () [] are ignored
# - Build-in datastructures: list, dict, set, tuple, iter


from typing import Iterator


def iter_example(max: int = 10) -> Iterator[int]:
    for c in range(0, max):
        yield c
#    raise StopIteration

def list_example(max: int = 10) -> list[int]:
    return [x for x in range(0, max)]

# print(list(range(1, 4)))

elements = (2*x for x in iter_example() if x > 3)
elements2 = iter(map(lambda x: 2*x, filter(lambda x: x > 3, iter_example())))


print(max(elements))
print(list(element))

# Two kind of operations on iterators:
# - Intermediate operations (e,g. map, filter) do not cause the iterator
#   to be evaluated
# - Terminal operations, e.g. max, for, list cause the iterator to be evaluated

# Library support: Iteratortools


def return_two(x: int, y: string) -> tuple[x, y]:
    return x, y


def swap(x, y):
    y, x = x, y



for x in elements:
    print(x, end=" ")  # Lazy evaluation

print(list_example())

def named_param(pos_param, *, hello, test) -> None:
    print(pos_param)
    print(hello)

named_param("Hello", test="help", hello=" World")
