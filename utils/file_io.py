import json
import csv

def read_json_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def read_csv_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    return rows

def write_csv_file(file_path,rows,fieldnames):
    with open(file_path,'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return True