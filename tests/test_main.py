import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from main import build_product_from_row

def test_build_product_from_row_with_valid_tax():
    row = {
        "name": " drone ",
        "destination": " Iran ",
        "category": " electronics ",
        "tax": "5000",
    }

    product = build_product_from_row(row)

    assert product.name == "DRONE"
    assert product.destination == "IRAN"
    assert product.category == "ELECTRONICS"
    assert product.tax == 5000

def test_build_product_from_row_with_invalid_tax():
    row = {
        "name": " drone ",
        "destination": " Iran ",
        "category": " electronics ",
        "tax": "abc",
    }

    product = build_product_from_row(row)

    assert product.tax == 0