from typing import Union
from aiogram import types
from aiogram.types import InputMedia
from keyboards.inline.catalog_inline_kb import categories_kb, subcategories_kb, items_kb, item_kb, menu_cd
from loader import dp, bot
from utils.db_api.quick_commands import get_item


@dp.message_handler(text="Каталог")
async def show_catalog(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_kb()
    photo_url = "https://sadovod-moskva.com/_sh/00/49c.jpg"
    if isinstance(message, types.Message):
        await message.answer_photo(photo=photo_url, caption="Выберите категорию:", reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        file = InputMedia(media=photo_url, caption="Выберите категорию:")
        await call.message.edit_media(file, reply_markup=markup)


async def list_subcategories(callback: types.CallbackQuery, category, **kwargs):
    markup = await subcategories_kb(category)
    spl = callback.data.split(':')[2]

    if spl == "Clothes":
        photo_url = "https://masteroff.org/wp-content/uploads/2021/12/upgrade-your-wardrobe-essentials-with-50-off-saturdays-nyc-10.jpg"
        file = InputMedia(media=photo_url, caption="Выберите категорию одежды:")
        await callback.message.edit_media(file, reply_markup=markup)

    elif spl == "Shoes":
        photo_url = "https://arta.online/upload/iblock/2e2/2e2bbeb6bb24b59e181d8090638bfd65.jpg"
        file = InputMedia(media=photo_url, caption="Выберите категорию обуви:")
        await callback.message.edit_media(file, reply_markup=markup)

    elif spl == "Bags":
        photo_url = "https://ae01.alicdn.com/kf/HLB1WXCxX0zvK1RkSnfoq6zMwVXa6/AEQUEEN.jpg"
        file = InputMedia(media=photo_url, caption="Выберите категорию сумок:")
        await callback.message.edit_media(file, reply_markup=markup)

    elif spl == "Accessories":
        photo_url = "https://sc02.alicdn.com/kf/HTB14Ftte2jM8KJjSZFy760dzVXaW/202120589/HTB14Ftte2jM8KJjSZFy760dzVXaW.png"
        file = InputMedia(media=photo_url, caption="Выберите категорию аксессуаров:")
        await callback.message.edit_media(file, reply_markup=markup)


async def list_items(callback: types.CallbackQuery, category, subcategory, **kwargs):
    markup = await items_kb(category=category, subcategory=subcategory)
    photo_url = "https://w7.pngwing.com/pngs/682/811/png-transparent-animation-direction-miscellaneous-hand-presentation.png"
    file = InputMedia(media=photo_url, caption=f"Выберите:")
    await callback.message.edit_media(file, reply_markup=markup)


async def show_item(callback: types.CallbackQuery, category, subcategory, item_id):
    markup = item_kb(category=category, subcategory=subcategory, item_id=item_id)
    item = await get_item(item_id)
    file = InputMedia(media=f'{item.photo_id}', caption=f'<b>Название:</b> {item.name}\n\n'
                                                        f'<b>Описание:</b> {item.description}\n\n'
                                                        f'<b>Наличие:</b> {item.count} шт.\n\n'
                                                        f'<b>Цена:</b> {item.price} руб.\n\n')
    await callback.message.edit_media(file, reply_markup=markup)


@dp.callback_query_handler(lambda call: "gotocatalog" in call.data)
async def go_to_catalog(call: types.CallbackQuery):
    await show_catalog(call.message)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    item_id = int(callback_data.get('item_id'))

    levels = {
        "0": list_categories,
        "1": list_subcategories,
        "2": list_items,
        "3": show_item
    }
    current_level_func = levels[current_level]

    await current_level_func(call, category=category, subcategory=subcategory, item_id=item_id)
