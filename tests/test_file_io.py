import json
import csv
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from utils.file_io import read_json_file,read_csv_file,write_csv_file,iter_csv_file

def test_read_json_file(tmp_path):
    file_path = tmp_path/'config.json'
    data = {
        "blacklist_products": ["DRONE", "CHIP"],
        "high_risk_countries": ["IRAN", "RUSSIA"],
    }
    file_path.write_text(json.dumps(data), encoding="utf-8")
    
    result = read_json_file(file_path)
    assert result == data

def test_read_csv_file(tmp_path):
    file_path=tmp_path/'product.csv'
    file_path.write_text( "name,destination,category,tax\n"
        "DRONE,IRAN,ELECTRONICS,5000\n"
        "BOOK,US,EDUCATION,100\n",
        encoding='utf-8')
    result = read_csv_file(file_path)
    assert result == [
        {
            "name": "DRONE",
            "destination": "IRAN",
            "category": "ELECTRONICS",
            "tax": "5000",
        },
        {
            "name": "BOOK",
            "destination": "US",
            "category": "EDUCATION",
            "tax": "100",
        },
    ]

def test_iter_csv_file(tmp_path):
    file_path=tmp_path/'product.csv'
    file_path.write_text( "name,destination,category,tax\n"
        "DRONE,IRAN,ELECTRONICS,5000\n"
        "BOOK,US,EDUCATION,100\n",
        encoding='utf-8')
    result = iter_csv_file(file_path)
    first_row = next(result)
    assert first_row == {
            "name": "DRONE",
            "destination": "IRAN",
            "category": "ELECTRONICS",
            "tax": "5000",
        }
    

def test_write_csv_file(tmp_path):
    file_path=tmp_path/'result.csv'
    rows = [
        {
            "name": "DRONE",
            "risk": "HIGH",
            "reason": "命中黑名单商品",
        },
        {
            "name": "BOOK",
            "risk": "LOW",
            "reason": "基础审核通过",
        },
    ]

    fieldnames = ["name", "risk", "reason"]

    result = write_csv_file(file_path,rows,fieldnames)
    assert result == True