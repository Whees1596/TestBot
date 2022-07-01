from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, sql, BigInteger, Float, String


class Payments(TimedBaseModel):
    __tablename__ = "payments"
    id = Column(BigInteger, primary_key=True)
    unique_id = Column(String(600), unique=True, nullable=False)
    user_id = Column(BigInteger)
    username = Column(String(100))
    amount = Column(Float)
    status = Column(String)
    bonus = Column(Float)
    items_id = Column(String)

    query: sql.Select