from models.product import AuditedProduct
def check_product_risk(product, config):
    blacklist_products = config["blacklist_products"]
    high_risk_countries = config["high_risk_countries"]

    product_hit = product.name in blacklist_products
    country_hit = product.destination in high_risk_countries

    if product_hit and country_hit:
        risk = "HIGH"
        reason = "命中黑名单商品和高风险国家"
    elif product_hit:
        risk = "HIGH"
        reason = "命中黑名单商品"
    elif country_hit:
        risk = "MEDIUM"
        reason = "命中高风险国家"
    else:
        risk = "LOW"
        reason = "基础审核通过"

    return AuditedProduct(
            name=product.name,
            destination=product.destination,
            category=product.category,
            tax=product.tax,
            risk=risk,
            reason=reason)
            
