# Auto-generated pytest tests for inventory_pricing_analysis
import importlib
mod = importlib.import_module('part2_tests.programs')
from part2_tests.programs.inventory_pricing_analysis import inventory_pricing_analysis


# ************** Iteration-0 ******************
def test_inventory_pricing_analysis_1():
    items = [("ItemA", 10, 75)]
    assert inventory_pricing_analysis(items) == ["ItemA"]

def test_inventory_pricing_analysis_2():
    items = [("ItemA", 1, 60)]  # Minimal quantity, mid-range price
    assert inventory_pricing_analysis(items) == ["ItemA"]




# ************** Iteration-1 ******************

def test_inventory_pricing_analysis_3():
    # Multi-item with different price categories, tie-breaking by quantity
    items = [
        ("ItemA", 10, 75),  # Standard
        ("ItemB", 15, 75),  # Standard, higher quantity
        ("ItemC", 5, 120),  # Premium
        ("ItemD", 2, 40)    # Discount
    ]
    # Sorted by price desc, quantity desc, name asc
    assert inventory_pricing_analysis(items) == ["ItemC","ItemB","ItemA","ItemD"]

def test_inventory_pricing_analysis_4():
 
    items = [
        ("ItemX", 8, 110),   # Premium
        ("ItemY", 12, 75),   # Standard
        ("ItemZ", 3, 45),    # Discount
        ("ItemW", 6, 75)     # Standard
    ]
    # Sorted by price descending, quantity descending, name ascending
    assert inventory_pricing_analysis(items) == ["ItemX","ItemY","ItemW","ItemZ"]





# ************** Iteration-2 ******************

def test_inventory_pricing_analysis_5():

    items = [
        ("ItemE", 5, 60),   # Standard
        ("ItemF", 10, 75),  # Standard
        ("ItemG", 3, 50)    # Standard, boundary
    ]
    # Sorted by price descending, quantity descending, name ascending
    assert inventory_pricing_analysis(items) == ["ItemF","ItemE","ItemG"]


def test_inventory_pricing_analysis_6():

    items = [
        ("ItemH", 7, 65),   # Standard
        ("ItemI", 12, 70),  # Standard
        ("ItemJ", 4, 55)    # Standard
    ]
    # Sorted by price descending, quantity descending, name ascending
    assert inventory_pricing_analysis(items) == ["ItemI","ItemH","ItemJ"]




# ************** Iteration-3 ******************

def test_inventory_pricing_analysis_7():

    items = [
        ("ItemE", 5, 50),  # Standard (boundary)
        ("ItemF", 5, 50),  # Standard (tie on quantity)
        ("ItemG", 0, 120)  # Out-of-stock, premium
    ]
    # Should include only E and F, sorted by name tie-break
    assert inventory_pricing_analysis(items) == ["ItemE","ItemF"]

    
def test_inventory_pricing_analysis_8():

    items = [
        ("ItemH", 3, 50),   # Standard (boundary)
        ("ItemI", 2, 50),   # Standard (tie on quantity)
        ("ItemJ", 0, 150)   # Out-of-stock, premium
    ]
    # Should include only H and I, sorted by name tie-break
    assert inventory_pricing_analysis(items) == ["ItemH","ItemI"]

