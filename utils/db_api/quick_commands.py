from asyncpg import UniqueViolationError

from utils.db_api.schemas.users import User
from utils.db_api.db_gino import db


async def get_user(user_id: int) -> User:
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def add_user(user_id: int, name: str, referal_id: int = None, balance: int = 0):
    try:
        user = User(user_id=user_id, name=name, referal_id=referal_id, balance=balance)
        await user.create()

    except UniqueViolationError:
        pass


async def count_refferals(user_id: int):
    count = await db.select([db.func.count(User.user_id)]).where(User.referal_id == user_id).gino.scalar()
    return count


async def change_user_balance(user_id: int, balance: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    await user.update(balance=balance).apply()
