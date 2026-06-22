from dataclasses import dataclass

@dataclass
class Product:
    name:str
    destination:str
    category:str
    tax:int
    
    def is_high_tax(self)->bool :
        return self.tax>=3000
    
    def get_summary(self) ->str:
        return f"{self.name} -> {self.destination} / {self.category} / tax={self.tax}"
    

@dataclass
class AuditedProduct(Product):
    risk:str
    reason:str
    
    def to_result_row(self):
        return {'name':self.name,'destination':self.destination,'category':self.category,'tax':self.tax,'risk':self.risk,'reason':self.reason}
