from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from .routes import orders, products

from apscheduler.schedulers.blocking import BlockingScheduler
from app.helpers.schedule import reset_default_inventory


tags_metadata = [
    {
        "name": "products",
        "description": "Manage products."
    },
    {
        "name": "orders",
        "description": "Operations with orders."
    },
]

app = FastAPI(
    title="Inventory System API",
    description="The api server for Inventory System",
    version="v1",
    openapi_tags=tags_metadata
)

app.include_router(products.router)
app.include_router(orders.router)

app = VersionedFastAPI(app, version_format='{major}', prefix_format='/api/v{major}')


@app.on_event("startup")
def init_scheduler():
    scheduler = BlockingScheduler()

    scheduler.add_job(reset_default_inventory, 'cron', day_of_week='*', hour=0, minute=0)
    
    scheduler.configure()
    scheduler.print_jobs()
    scheduler.start()
