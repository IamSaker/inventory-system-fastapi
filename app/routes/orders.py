from fastapi import Depends, APIRouter, HTTPException, status
from fastapi_versioning import version
from typing import List
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import Order
from app.crud import order as crud_order
from app.helpers.orders import check_order_status, pre_order, order_date
from app.helpers.products import get_default_inventory, get_current_inventory, reduce_current_inventory

router = APIRouter()


@router.get("/order/{id}", response_model=Order)
@version(1)
async def get_all_products(id: int, db: Session = Depends(get_db)) -> Order:
    return crud_order.get_order(db, id)


@router.get("/orders", response_model=List[Order])
@version(1)
async def get_all_products(db: Session = Depends(get_db)) -> List[Order]:
    return crud_order.get_orders(db)
  

@router.post("/orders", status_code=status.HTTP_201_CREATED)
@version(1)
async def create_order(order_to_create: Order, db: Session = Depends(get_db)):
    total = order_to_create.total
    product_id = order_to_create.product_id

    quantity = get_default_inventory(db, product_id)
    current = get_current_inventory(db, product_id)
    is_preorder = check_order_status(db, total, product_id)

    if is_preorder:
        pre_order(db, total, product_id)
        reduce_current_inventory(db, quantity, quantity, product_id)
    else:
        order_to_create.preorder_date = order_date(0)
        crud_order.create_order(db, order_to_create)
        reduce_current_inventory(db, total, current, product_id)
    return {}
