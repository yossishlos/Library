import logging
from fastapi import FastAPI
from routes import book_routes
from database.db_connection import DB

logging.basicConfig(
    level=logging.INFO,
    format="| %(asctime)s | %(levelname)s | %(message)s |",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)

db = DB()
db.get_connection()
db.create_table()
db.disconnect()

app = FastAPI()
app.include_router(book_routes.router)