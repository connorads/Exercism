"""Functions to keep track and alter inventory."""

Items = list[str]
Inventory = dict[str, int]


def create_inventory(items: Items) -> Inventory:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory: Inventory = {}
    return add_items(inventory, items)


def add_items(inventory: Inventory, items: Items) -> Inventory:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory: Inventory, items: Items) -> Inventory:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: Inventory, item: str) -> Inventory:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: Inventory) -> list[tuple[str, int]]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(k, v) for k, v in inventory.items() if v > 0]
