# Python Cookbook, 3rd Ed.
#
# Chapter: Function Definitions
# Recipe: Function parameters and type hints

from typing import reveal_type


def hex2rgb(hx_int: int | str) -> tuple[int, int, int]:
    if isinstance(hx_int, str):
        if hx_int[0] == "#":
            hx_int = int(hx_int[1:], 16)
        else:
            hx_int = int(hx_int, 16)
    # Use mypy to reveal the type of hx_int
    # recipe_01_reveal.py:15: note: Revealed type is "builtins.int"
    reveal_type(hx_int)
    r, g, b = (hx_int >> 16) & 0xFF, (hx_int >> 8) & 0xFF, hx_int & 0xFF
    return r, g, b

if __name__ == '__main__':
    print(hex2rgb(0x00FF00))
    print(hex2rgb("#00FF00"))
    print(hex2rgb("00FF00"))