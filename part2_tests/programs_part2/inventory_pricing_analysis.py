# part2_tests/programs/inventory_pricing_analysis.py

def inventory_pricing_analysis(items):
    """
    items: list of tuples (name:str, quantity:int, price:float)
    
    Returns a sorted list of item names that meet criteria:
    - quantity > 0
    - price within allowed ranges
        - price > 100 → premium
        - price >=50 → standard
        - price <50 → discount
    Sorted by price descending, then quantity descending, then name ascending.
    """
    valid_items = []
    for name, quantity, price in items:
        if quantity > 0:
            if price > 100:
                valid_items.append((name, quantity, price, "Premium"))
            elif price >= 50:
                valid_items.append((name, quantity, price, "Standard"))
            else:
                valid_items.append((name, quantity, price, "Discount"))
        else:
            # Out of stock branch
            continue

    # Sort by price desc, quantity desc, name asc
    valid_items.sort(key=lambda x: (-x[2], -x[1], x[0]))
    return [name for name, _, _, _ in valid_items]
