from fastapi import Depends, APIRouter, HTTPException, status
from fastapi_versioning import version
from typing import List
from sqlalchemy.orm import Session

from app.schemas import Product
from app.crud import product as crud_product
from app.db import get_db

router = APIRouter()


@router.get("/products", response_model=List[Product])
@version(1)
async def get_all_products(db: Session = Depends(get_db)) -> List[Product]:
    return crud_product.get_products(db)
  

@router.post("/products", status_code=status.HTTP_201_CREATED)
@version(1)
async def create_product(product_to_create: Product, db: Session = Depends(get_db)):
    if crud_product.is_product_existed(db, name=product_to_create.name):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'product {product_to_create.name} is already existed!',
        )
  
    crud_product.create_product(db, product_to_create)
    return {}


@router.patch("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
@version(1)
async def update_product(id: int, data_to_update: Product, db: Session = Depends(get_db)):
    if not crud_product.is_product_existed(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'product {data_to_update.name} is not found!',
        )
  
    crud_product.update_product(db, id, data_to_update)


@router.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
@version(1)
async def delete_product(id: int, db: Session = Depends(get_db)):
    if crud_product.is_product_existed(db, id):
        crud_product.delete_product(db, id)
