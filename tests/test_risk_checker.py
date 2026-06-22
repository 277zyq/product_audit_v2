import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from models.product import Product
from services.risk_checker import check_product_risk

def test_blacklist_and_high_risk_country():
     product = Product("DRONE", "IRAN", "ELECTRONICS", 5000)
     config = {
        "blacklist_products": ["DRONE", "CHIP"],
        "high_risk_countries": ["IRAN", "RUSSIA"],
    }

     result = check_product_risk(product, config)

     assert result.risk== 'HIGH'
     assert result.reason == '命中黑名单商品和高风险国家' 

def test_normal_product():
    product = Product("BOOK", "US", "EDUCATION", 100)
    config = {
        "blacklist_products": ["DRONE", "CHIP"],
        "high_risk_countries": ["IRAN", "RUSSIA"],
    }

    result = check_product_risk(product, config)

    assert result.risk == "LOW"
    assert result.reason == "基础审核通过"