class Product:
    def __init__(self,name,destination,category,tax):
        self.name=name
        self.destination=destination
        self.category=category
        self.tax=tax
    
    def is_high_tax(self):
        return self.tax>=3000
    
    def get_summary(self):
        return f"{self.name} -> {self.destination} / {self.category} / tax={self.tax}"