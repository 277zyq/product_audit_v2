from pathlib import Path

from models.product import Product
from services.risk_checker import check_product_risk
from utils.file_io import read_csv_file, read_json_file, write_csv_file

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

CONFIG_PATH = DATA_DIR / "risk_config.json"
PRODUCTS_PATH = DATA_DIR / "products.csv"
OUTPUT_PATH = OUTPUT_DIR / "product_risk_result.csv"

def build_product_from_row(row):
    return Product(
        name=row["name"].strip().upper(),
        destination=row["destination"].strip().upper(),
        category=row["category"].strip().upper(),
        tax=int(row["tax"]),
    )

def main():
    config = read_json_file(CONFIG_PATH)
    rows = read_csv_file(PRODUCTS_PATH)

    results=[]
    
    for row in rows:
        product = build_product_from_row(row)
        result = check_product_risk(product,config)
        results.append(result)
    OUTPUT_DIR.mkdir(exist_ok=True)
    fieldnames = ["name", "destination", "category", "tax", "risk", "reason"]
    write_csv_file(OUTPUT_PATH, results, fieldnames)

    print(f'审核完成，共输出{len(results)}条记录')
    print(f'输出文件{OUTPUT_PATH}')

if __name__ == '__main__':
    main() 

