import sys
from pathlib import Path
from utils.decorators import timer
import pytest

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from main import CONFIG_PATH, OUTPUT_PATH, PRODUCTS_PATH, build_product_from_row, parse_args

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


def test_parse_args_with_default_values():
    args = parse_args([])

    assert args.config == CONFIG_PATH
    assert args.input == PRODUCTS_PATH
    assert args.output == OUTPUT_PATH


def test_parse_args_with_custom_values():
    args = parse_args([
        "--config",
        "custom_config.json",
        "--input",
        "custom_products.csv",
        "--output",
        "custom_result.csv",
    ])

    assert args.config == "custom_config.json"
    assert args.input == "custom_products.csv"
    assert args.output == "custom_result.csv"

def test_decorator():

    @timer
    def add(a,b):
        return a+b
    
    a=add(1,2)

    assert a == 3

def test_build_product_from_row_without_tax():
    row = {
        "name": "drone",
        "destination": "Iran",
        "category": "electronics",
    }

    with pytest.raises(KeyError):
        build_product_from_row(row)
