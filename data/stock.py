from dataclasses import dataclass


@dataclass
class Material:
    item_name: str
    current_stock: int
    color: str
    stock_position: tuple[int, int]


def new_material(name: str, color: str, stock_position: tuple[int, int]) -> Material:
    return Material(name, 0, color, stock_position)
