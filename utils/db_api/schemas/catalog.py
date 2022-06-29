from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, String, sql, BigInteger, Float, Integer


class Catalog(TimedBaseModel):
    __tablename__ = "catalog"
    id_item = Column(BigInteger, primary_key=True, autoincrement=True)
    category_code = Column(String(20))
    category_name = Column(String(100))
    subcategory_code = Column(String(20))
    subcategory_name = Column(String(100))
    name = Column(String(50))
    photo_id = Column(String(1000))
    description = Column(String(255))
    price = Column(Float)
    count = Column(Integer)

    query: sql.Select