from sqlalchemy.orm import Session
from app.schemas import PreOrder, CurrentInventoryUpdateToDB
from app.crud import order as crud_order, product as crud_product
from app.helpers.products import get_current_inventory, get_default_inventory
from datetime import date, datetime, timedelta


def order_date(day: int):
    _date = date.today() + timedelta(days=day)
    return _date.strftime("%Y-%m-%d")


def calculus_order_quantity(db: Session, total: int, product_id: int):
    date, quantity, flag = [], [], []
    current = get_current_inventory(db, product_id)
    default = get_default_inventory(db, product_id)

    total -= current
    quotient = total // default
    remainder = total % default

    times = quotient + 1 if remainder == 0 else quotient + 2
    for time in range(times):
        date.append(order_date(time))

    quantity.append(current)
    flag.append(False)
    if quotient == 0:
        quantity.append(remainder)
        flag.append(True)
    else:
        for i in range(quotient):
            quantity.append(default)
            flag.append(True)
        if remainder != 0:
            quantity.append(remainder)
            flag.append(True)
    
    return date, quantity, flag


def check_order_status(db: Session, total: int, product_id: int):
    is_preorder = False
    current = get_current_inventory(db, product_id)
    if(current < total):
        is_preorder = True
    return is_preorder


def check_pre_order(db: Session, date: str, product_id: int):
    default = get_default_inventory(db, product_id)
    preorder_amount = crud_order.get_specific_order_amount(db, date, date)
    current = default - preorder_amount
    quantity = CurrentInventoryUpdateToDB(
        current_inventory=current
    )
    crud_product.update_product(db, product_id, quantity)


def pre_order(db: Session, total: int, product_id: int):
    dates, quantities, flags = calculus_order_quantity(db, total, product_id)

    for i in range(len(dates)):
        preorder_to_create = PreOrder(
            product_id = product_id,
            total = quantities[i],
            is_preorder = flags[i],
            preorder_date = dates[i]
        )
        crud_order.create_order(db, preorder_to_create)
