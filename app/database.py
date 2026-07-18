"""Simple in-memory store for learning purposes."""

_items: list[dict] = []
_next_id = 1


def reset() -> None:
    global _items, _next_id
    _items = []
    _next_id = 1


def get_all_items() -> list[dict]:
    return list(_items)


def add_item(name: str) -> dict:
    global _next_id
    item = {"id": _next_id, "name": name}
    _items.append(item)
    _next_id += 1
    return item


def get_item(item_id: int) -> dict | None:
    for item in _items:
        if item["id"] == item_id:
            return item
    return None
