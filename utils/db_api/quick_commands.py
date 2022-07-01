from typing import List
from asyncpg import UniqueViolationError
from sqlalchemy import and_

from utils.db_api.schemas.users import User
from utils.db_api.schemas.catalog import Catalog
from utils.db_api.schemas.basket import Basket
from utils.db_api.schemas.payments import Payments
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


async def get_item(item_id):
    item = await Catalog.query.where(Catalog.id_item == item_id).gino.first()
    return item


async def get_items(category_code, subcategory_code) -> List[Catalog]:
    items = await Catalog.query.where(
        and_(Catalog.category_code == category_code, Catalog.subcategory_code == subcategory_code)
    ).gino.all()

    return items


async def get_categories() -> List[Catalog]:
    return await Catalog.query.distinct(Catalog.category_code).gino.all()


async def get_subcategories(category) -> List[Catalog]:
    return await Catalog.query.distinct(Catalog.subcategory_code).where(Catalog.category_code == category).gino.all()


async def count_items(category_code, subcategory_code=None):
    conditions = [Catalog.category_code == category_code]

    if subcategory_code:
        conditions.append(Catalog.subcategory_code == subcategory_code)

    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()

    return total


async def add_item(category_name: str, subcategory_name: str, category_code: str, subcategory_code: str,
                   name: str, photo_id: str, description: str, price: int, count: int):
    try:
        item = Catalog(category_name=category_name, subcategory_name=subcategory_name, category_code=category_code,
                       subcategory_code=subcategory_code, name=name, photo_id=photo_id,
                       description=description, price=price, count=count)
        await item.create()

    except UniqueViolationError:
        pass


async def show_user_basket(user_id: int) -> List[Basket]:
    basket = await Basket.query.where(Basket.user_id == user_id).gino.all()
    return basket


async def create_user_basket(user_id: int, item_id: int, item_price: float):
    try:
        basket = Basket(user_id=user_id, item_id=item_id, item_price=item_price)
        await basket.create()

    except UniqueViolationError:
        pass


async def get_items_basket(item_id: int) -> List[Catalog]:
    items = await Catalog.query.where(
        and_(Catalog.id_item == item_id)
    ).gino.all()

    return items


async def count_items_id_basket(user_id: int, item_id: int):
    count = await db.select([db.func.count(Basket.user_id)]).where(
        and_(Basket.item_id == item_id, Basket.user_id == user_id)).gino.scalar()
    return count


async def delete_user_basket(user_id: int):
    await Basket.delete.where(Basket.user_id == user_id).gino.status()


async def add_payment(unique_id: str, user_id: int, username: str, amount: float, status: str, bonus: float,
                      items_id: str):
    item = Payments(unique_id=unique_id, user_id=user_id, username=username, amount=amount, status=status, bonus=bonus,
                    items_id=items_id)
    await item.create()


async def change_status_payment(id_payments: int, status: str):
    user = await Payments.query.where(Payments.id == id_payments).gino.first()
    await user.update(status=status).apply()


async def get_payment_unique(unique_id: str):
    payment = await Payments.query.where(Payments.unique_id == unique_id).gino.first()
    return payment


async def get_payment(id_payments: int):
    payment = await Payments.query.where(Payments.id == id_payments).gino.first()
    return payment


async def get_all_history_payment_user(user_id: int) -> List[Payments]:
    payments = await Payments.query.where(Payments.user_id == user_id).gino.all()
    return payments
