from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, sql, BigInteger, Float


class Basket(TimedBaseModel):
    __tablename__ = "basket"
    user_id = Column(BigInteger)
    item_id = Column(BigInteger)
    item_price = Column(Float)

    query: sql.Select