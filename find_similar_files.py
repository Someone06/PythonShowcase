from pathlib import Path
from typing import Callable, Iterable, Iterator
from pprint import pprint as pretty_print
from collections import defaultdict


# Python if statements:
# if 0 not in {0, 1, 2} -> false
# if "abc" is not None -> true
# if "0" == "1"  -> false
# if "str" in "string" -> true
# if "abc" -> true
# if "" -> false
# if 0 -> false
# if 1 -> true


# Default dict associates a default value with key, when trying to read a value
# for a key, which is not yet present in the dictionary.
def group_by_suffix(file_names: Iterable[Path]) -> dict[str, set[str]]:
    result = defaultdict(lambda: set())
    for file_name in file_names:
        if file_name.stem not in result:
            result[file_name.stem] = set()
        result[file_name.stem].add(file_name.suffix)

    return result

def get(d: dict[str, set[str]], defaultValueFactory: Callable[[int, str], set[str]], key: str) -> set[str]:
   if key not in d:
       d[key] = defaultValueFactory()
   return d[key]


def f(a: str, b: str, c: str) -> list[str]:
    return [a, b , c]


def f_test() -> None:
    l = ["a", "b", "c"]
    #res = f(l[0], l[1], l[2])
    res = f(*l)
    pretty_print(res)

def g(*args, **kwargs) -> None:
    pass

f_test()



# Pathlib can be used to work with file system paths
def get_files_in_cwd() -> Iterator[Path]:
    return Path.cwd().iterdir()



def main():
    cwd = Path.cwd()
    paths = [cwd / "a.test", cwd / "a.help"]
    res = group_by_suffix(paths)
    pretty_print(res)

    files_in_cwd = get_files_in_cwd()
    res = group_by_suffix(files_in_cwd)
    pretty_print(res)


if __name__ == "__main__":
    main()
