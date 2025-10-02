class MenuItem:
    def __init__(self, code : str, name : str, price : float, category : str ):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
    
    def __repr__(self):
        return f"{self.code} - {self.name} - {self.category} - ${self.price:.2f}"

class Menu:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item : MenuItem):
        # use code as the unique key; check membership by code
        if item.code not in self.items:
            self.items[item.code] = item
    
    def list_items(self):
        return list(self.items.values())
    
    def get_item(self, code : str):
         return self.items.get(code)

    

    
    