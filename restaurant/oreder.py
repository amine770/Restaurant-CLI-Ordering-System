from .menu import MenuItem
from typing import List
import itertools

_order_id_gen = itertools.count(1)

class OrderItem:
    def __init__(self, menu_item : MenuItem, qty : int = 1, modifiers : dict=None):
        self.menu_item = menu_item
        self.qty = qty
        self.modifiers = modifiers or {}

    def item_total(self):
        total = sum(self.modifiers.values())
        return (self.menu_item.price + total) * self.qty
    
    def to_dict(self):
        return {
            "code" : self.menu_item.code,
            "name" : self.menu_item.name,
            "unit_price" : self.menu_item.price,
            "qty" : self.qty,
            "category" : self.menu_item.category,
            "modifiers" : self.modifiers,
            "total" : self.item_total()
        }

class Order:
    VALID_STATUSES = ("placed", "preparing", "ready", "served", "cancelled")

    def __init__(self, customer_name : str = "guest"):
        self.id = next(_order_id_gen)
        self.customer_name = customer_name
        self.state = "placed"
        self.items : List[OrderItem] = []
    
    def add_item(self, order_item : OrderItem ):
        self.items.append(order_item)
    
    def set_state(self, state: str):
        if state in self.VALID_STATUSES:
            self.state = state
    
    def remove_item(self, index: int):
        if 0<= index < len(self.items):
            self.items.pop(index)
    
    def total(self, tax: float = 0.0, dicount: float = 0.0):
        subtotal = sum(item.item_total() for item in self.items)
        after_dicount = subtotal - dicount
        tax = (after_dicount * tax) / 100
        return after_dicount + tax
    
    def to_dict(self):
        return {
            "id" : self.id,
            "customer_name" : self.customer_name,
            "state" : self.state,
            "items" : [item.to_dict() for item in self.items],
            "total" : self.total()
        }
        
        

