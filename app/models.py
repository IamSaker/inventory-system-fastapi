import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base
from .helpers.sqlalchemy.utcnow import utcnow


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=True)
    current_inventory = Column(Integer)
    default_inventory = Column(Integer)

    order = relationship("Order", uselist=False, back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    total = Column(Integer)
    is_preorder = Column(Boolean, nullable=False, default=False)
    preorder_date = Column(Date, index=True)
    created_at = Column(DateTime, server_default=utcnow())

    product = relationship("Product", back_populates="order")
