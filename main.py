from pathlib import Path
from models.product import Product
from services.risk_checker import check_product_risk
from utils.file_io import read_csv_file, read_json_file, write_csv_file
import logging
import argparse



logging.basicConfig(level=logging.INFO,format='%(levelname)s:%(message)s')

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

CONFIG_PATH = DATA_DIR / "risk_config.json"
PRODUCTS_PATH = DATA_DIR / "products.csv"
OUTPUT_PATH = OUTPUT_DIR / "product_risk_result.csv"

def parse_args(argv:list[str]=None):
    parser = argparse.ArgumentParser(description='商品风险审查工具')
    parser.add_argument('-c','--config',
                        default=CONFIG_PATH,
                        help='风险审查配置json清单')
    parser.add_argument('-i','--input',default=PRODUCTS_PATH,help='产品csv')
    parser.add_argument('-o','--output',default=OUTPUT_PATH,help='审查输出')
    return parser.parse_args(argv)
                        
                        



def build_product_from_row(row):
    try:
        tax = int(row['tax'])
    except ValueError:
        tax = 0
    return Product(
        name=row["name"].strip().upper(),
        destination=row["destination"].strip().upper(),
        category=row["category"].strip().upper(),
        tax=tax,
    )

def main():
    args = parse_args()
    config = read_json_file(args.config)
    rows = read_csv_file(args.input)

    results=[]
    
    for row in rows:
        product = build_product_from_row(row)
        result = check_product_risk(product,config)
        results.append(result.to_result_row())
    OUTPUT_DIR.mkdir(exist_ok=True)
    fieldnames = ["name", "destination", "category", "tax", "risk", "reason"]
    write_csv_file(args.output, results, fieldnames)

    logging.info(f'审核完成，共输出{len(results)}条记录')
    logging.info(f'输出文件{args.output}')

if __name__ == '__main__':
    main() 

