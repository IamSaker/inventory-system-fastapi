from sqlalchemy.orm import Session
from app.schemas import CurrentInventoryUpdateToDB
from app.crud import product as crud_product


def get_current_inventory(db: Session, id: int):
    inventorys = crud_product.get_product(db, id, name="")
    return inventorys.__dict__["current_inventory"]


def get_default_inventory(db: Session, id: int):
    inventorys = crud_product.get_product(db, id, name="")
    return inventorys.__dict__["default_inventory"]


def reduce_current_inventory(db: Session, order_quantity: int, current_quantity: int, product_id: int):
    quantity = current_quantity - order_quantity
    reduce_amount = CurrentInventoryUpdateToDB(
        current_inventory=quantity
    )
    crud_product.update_product(db, product_id, reduce_amount)


def reset_current_inventory(db: Session, id: int):
    default = get_default_inventory(db, id)
    reset = CurrentInventoryUpdateToDB(
        current_inventory=default
    )
    crud_product.update_product(db, id, reset)
