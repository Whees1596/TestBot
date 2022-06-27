from typing import List
from asyncpg import UniqueViolationError
from sqlalchemy import and_

from utils.db_api.schemas.users import User

"""Операции с пользователями"""


async def user_exists(user_id) -> User:
    result = await User.query.where(User.user_id == user_id).gino.first()
    return result


async def add_user(user_id: int, name: str, referal_id: int = None):
    try:
        user = User(user_id=user_id, name=name, referal_id=referal_id)
        await user.create()

    except UniqueViolationError:
        pass
