from sqlalchemy.orm import Session
from app import models, schemas


def get_product(db: Session, id: int, name: str) -> models.Product:
    if id != 0:
        return db.query(models.Product).filter(models.Product.id == id).first()
    elif id == 0 and name != "":
        return db.query(models.Product).filter(models.Product.name == name).first()
    return None


def get_products(db: Session) -> models.Product:
    return db.query(models.Product).all()


def get_product_ids(db: Session) -> models.Product:
    return db.query(models.Product.id).order_by(models.Product.id.asc()).all()


def create_product(db: Session, product_data: schemas.Product):
    product_to_create = models.Product(
        name=product_data.name,
        current_inventory=product_data.current_inventory,
        default_inventory=product_data.default_inventory,
    )

    db.add(product_to_create)
    db.commit()


def update_product(db: Session, id: int, user_data_to_update: schemas.Product):
    updated_user_data = schemas.ProductUpdateToDB(
        **user_data_to_update.dict()
    ).dict(exclude_none=True)
    
    product = db.query(models.Product).filter(models.Product.id == id).one()  
    for attr in updated_user_data:
        setattr(product, attr, updated_user_data[attr])

    db.commit()


def delete_product(db: Session, id: int):
    db.query(models.Product).filter(models.Product.id == id).delete()
    db.commit()


def is_product_existed(db: Session, id: int = 0, name: str = "") -> bool:
    return True if get_product(db, id, name) is not None else False
