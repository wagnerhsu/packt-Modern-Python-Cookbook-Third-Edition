from typing import NamedTuple

class RGB(NamedTuple):
    red: int
    green: int
    blue: int

if __name__ == "__main__":
    rgb = RGB(0, 255, 0)
    print(rgb)
    print(f"red: {rgb.red}, green: {rgb.green}, blue: {rgb.blue}")
    print(f"red: {rgb[0]}, green: {rgb[1]}, blue: {rgb[2]}")
    r, g, b = rgb
    print(f"red: {r}, green: {g}, blue: {b}")
    r, g, b = (0, 255, 0)
    rgb = RGB(r, g, b)
    print(rgb)
    print(f"red: {rgb.red}, green: {rgb.green}, blue: {rgb.blue}")
    print(f"red: {rgb[0]}, green: {rgb[1]}, blue: {rgb[2]}")
    r, g, b = rgb
    print(f"red: {r}, green: {g}, blue: {b}")
    r, g, b = (0, 255, 0)
    rgb = RGB(red=r, green=g, blue=b)
    print(rgb)
    print(f"red: {rgb.red}, green: {rgb.green}, blue: {rgb.blue}")
    print(f"red: {rgb[0]}, green: {rgb[1]}, blue: {rgb[2]}")
    r, g, b = rgb
    print(f"red: {r}, green: {g}, blue: {b}")
    r, g, b = (0, 255, 0)
    rgb = RGB(green=g, red=r, blue=b)
    print(rgb)
    print(f"red: {rgb.red}, green: {rgb.green}, blue: {rgb.blue}")
    print(f"red: {rgb[0]}, green: {rgb[1]}, blue: {rgb[2]}")
    r, g, b = rgb
    print(f"red: {r}, green: {g}, blue: {b}")
    r, g, b = (0, 255, 0)
    rgb = RGB(red=r, blue=b, green=g)
    print(rgb)
    print(f"red: {rgb.red}, green: {rgb.green}, blue: {rgb.blue}")
    print(f"red: {rgb[0]}, green: {rgb[1]}, blue: {rgb[2]}")