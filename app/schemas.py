from typing import Optional, Dict, List
from pydantic import BaseModel
from datetime import datetime


class Product(BaseModel):
    id: Optional[int]
    name: Optional[str] = ""
    current_inventory: int
    default_inventory: int

    class Config:
        orm_mode = True


class ProductUpdateToDB(BaseModel):
    name: Optional[str] = None
    current_inventory: Optional[int]
    default_inventory: Optional[int]


class CurrentInventoryUpdateToDB(BaseModel):
    current_inventory: int


class Order(BaseModel):
    id: Optional[int]
    product_id: int
    total: int
    is_preorder: Optional[bool] = False
    preorder_date: Optional[str] 

    class Config:
        orm_mode = True


class PreOrder(BaseModel):
    product_id: int
    total: int
    is_preorder: bool
    preorder_date: str 
