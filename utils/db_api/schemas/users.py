from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql


class User(TimedBaseModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    name = Column(String(100))
    referal_id = Column(BigInteger)
    balance = Column(BigInteger)

    query: sql.Select