from settings import settings
import databases
import sqlalchemy

from sqlalchemy import create_engine

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
customers = sqlalchemy.Table(
    "customers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(128),nullable=False, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String(32),nullable=False),
    sqlalchemy.Column("surname", sqlalchemy.String(128),nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String(256),nullable=False)
)

goods = sqlalchemy.Table(
    "goods",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(128), nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String(1024), nullable=False),
    sqlalchemy.Column("price", sqlalchemy.Float(precision=2), nullable=False)
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("customer_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('customers.id')),
    sqlalchemy.Column("goods_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('goods.id')),
    sqlalchemy.Column("order_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String(1024))
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)