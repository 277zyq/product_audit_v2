from fastapi import FastAPI
from pydantic import BaseModel
from main import CONFIG_PATH
from models.product import Product
from services.risk_checker import check_product_risk
from utils.file_io import read_json_file

app=FastAPI()

@app.get('/health')
def check_health():
    return {'status':'good'}

class ProductRequest(BaseModel):
    name:str
    destination:str
    category:str
    tax:int

@app.post('/audit')
def audit_product(request:ProductRequest):
    config = read_json_file(CONFIG_PATH)

    product = Product(
        name=request.name.strip().upper(),
        destination=request.destination.strip().upper(),
        category=request.category.strip().upper(),
        tax=request.tax,
    )

    result = check_product_risk(product, config)

    return result.to_result_row()