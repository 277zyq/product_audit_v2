from dataclasses import dataclass

@dataclass
class Product:
    name:str
    destination:str
    category:str
    tax:int
    
    def is_high_tax(self):
        return self.tax>=3000
    
    def get_summary(self):
        return f"{self.name} -> {self.destination} / {self.category} / tax={self.tax}"