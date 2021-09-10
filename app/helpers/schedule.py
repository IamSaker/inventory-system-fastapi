from sqlalchemy.orm import Session
from app.crud.product import get_product_ids
from app.helpers.orders import order_date, check_pre_order


def reset_default_inventory(db: Session):
    product_ids = get_product_ids(db)
    date = order_date(0)
    for product_id in product_ids:
        check_pre_order(db, date, product_id)
