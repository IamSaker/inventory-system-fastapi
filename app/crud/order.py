from sqlalchemy.orm import Session
from app import models, schemas


def get_order(db: Session, id: int) -> models.Order:
    return db.query(models.Order).filter(models.Order.id == id).first()


def get_orders(db: Session) -> models.Order:
    return db.query(models.Order).all()


def get_specific_order_amount(db: Session, first_date: str, second_date: str):
    return db.query(models.Order).filter(models.Order.preorder_date.between(first_date, second_date)).count()


def create_order(db: Session, order_data: schemas.Order):
    order_to_create = models.Order(
        product_id=order_data.product_id,
        total=order_data.total,
        is_preorder=order_data.is_preorder,
        preorder_date=order_data.preorder_date
    )

    db.add(order_to_create)
    db.commit()
