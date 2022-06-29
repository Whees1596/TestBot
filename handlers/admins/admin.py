from aiogram import types
from loader import dp, bot
from states import FSMadmin
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default import admin_menu
from keyboards.inline import *
from utils.db_api import quick_commands as commands

ID = None


# Получаем ID текущего модератора
@dp.message_handler(commands=['join_admin'])
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Вы вошли в админ-панель!', reply_markup=await admin_menu())
    await message.delete()

    # Выход из состояний


@dp.message_handler(state='*', commands='Отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_FSM(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer('Добавление отменено!')
        await message.delete()

        # Начало диалога загрузки нового товара


@dp.message_handler(text="Добавить товар", state=None)
async def add_new_product(message: types.Message):
    if message.from_user.id == ID:
        await FSMadmin.category_name.set()
        await message.answer('Выбери категорию:',
                             reply_markup=await select_category_admin_inline_kb())
        await message.delete()


# Ловим первый ответ "Категорию" и пишем в словарь
@dp.callback_query_handler(lambda callback: "clothes" or "shoes" or "bags" or "accessories" in callback.data,
                           state=FSMadmin.category_name)
async def select_category(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == ID:
        async with state.proxy() as data:
            if callback.data == "clothes":
                data['category_name'] = "Одежда"
            elif callback.data == "shoes":
                data['category_name'] = "Обувь"
            elif callback.data == "bags":
                data['category_name'] = "Сумки"
            elif callback.data == "accessories":
                data['category_name'] = "Аксессуары"
        await FSMadmin.next()
        if callback.data == "clothes":
            await callback.message.answer(text='Теперь выбери подкатегорию:',
                                          reply_markup=await select_sub_category_clothes_admin_inline_kb())

        elif callback.data == "shoes":
            await callback.message.answer(text='Теперь выбери подкатегорию:',
                                          reply_markup=await select_sub_category_shoes_admin_inline_kb())

        elif callback.data == "bags":
            await callback.message.answer(text='Теперь выбери подкатегорию:',
                                          reply_markup=await select_sub_category_bags_admin_inline_kb())

        elif callback.data == "accessories":
            await callback.message.answer(text='Теперь выбери подкатегорию:',
                                          reply_markup=await select_sub_category_accessories_admin_inline_kb())
        else:
            await callback.message.answer(text='Такой подкатегории нет.')
            return
    await callback.message.delete()


# Ловим второй ответ "Подкатегорию" и пишем в словарь
# Подкатегории для категории "Одежда"
@dp.callback_query_handler(lambda callback: "jeans_and_trousers" or "hoodies_and_sweaters" or "t-shirts"
                                            or "outerwear" or "shorts" or "sports" in callback.data,
                           state=FSMadmin.subcategory_name)
async def select_sub_category_clothes(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == ID:
        async with state.proxy() as data:
            if callback.data == "jeans_and_trousers":
                data['subcategory_name'] = "Джинсы и брюки"
            elif callback.data == "hoodies_and_sweaters":
                data['subcategory_name'] = "Толстовки и свитеры"
            elif callback.data == "shirts":
                data['subcategory_name'] = "Футболки"
            elif callback.data == "outerwear":
                data['subcategory_name'] = "Верхняя одежда"
            elif callback.data == "shorts":
                data['subcategory_name'] = "Шорты"
            elif callback.data == "sports":
                data['subcategory_name'] = "Спортивная"
        await FSMadmin.next()
        await callback.message.answer('Введи code категории:')
    await callback.message.delete()


    # Подкатегории для категории "Обувь"
@dp.callback_query_handler(lambda callback: "sneakers" or "low_sneakers" or "flip-flops"
                                            or "off_shoes" or "boots" in callback.data,
                           state=FSMadmin.subcategory_name)
async def select_sub_category_shoes(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == ID:
        async with state.proxy() as data:
            if callback.data == "sneakers":
                data['subcategory_name'] = "Кроссовки"
            elif callback.data == "low_sneakers":
                data['subcategory_name'] = "Кеды"
            elif callback.data == "flip-flops":
                data['subcategory_name'] = "Шлепанцы"
            elif callback.data == "off_shoes":
                data['subcategory_name'] = "Туфли"
            elif callback.data == "boots":
                data['subcategory_name'] = "Ботинки"
        await FSMadmin.next()
        await callback.message.answer('Введи code категории:')
    await callback.message.delete()


    # Подкатегории для категории "Сумки"
@dp.callback_query_handler(lambda callback: "backpacks" or "sub_bags" or '"bananas"' in callback.data,
                           state=FSMadmin.subcategory_name)
async def select_sub_category_bags(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == ID:
        async with state.proxy() as data:
            if callback.data == "backpacks":
                data['subcategory_name'] = "Рюкзаки"
            elif callback.data == "sub_bags":
                data['subcategory_name'] = "Сумки"
            elif callback.data == '"bananas"':
                data['subcategory_name'] = "Бананки"
        await FSMadmin.next()
        await callback.message.answer('Введи code категории:')
    await callback.message.delete()


    # Подкатегории для категории "Аксессуары"
@dp.callback_query_handler(lambda callback: "watch" or "belts" or 'glasses' in callback.data,
                           state=FSMadmin.subcategory_name)
async def select_sub_category_accessories(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == ID:
        async with state.proxy() as data:
            if callback.data == "watch":
                data['subcategory_name'] = "Часы"
            elif callback.data == "belts":
                data['subcategory_name'] = "Ремни"
            elif callback.data == "glasses":
                data['subcategory_name'] = "Очки"
        await FSMadmin.next()
        await callback.message.answer('Введи code категории:')
    await callback.message.delete()


# Ловим третий ответ "code категории" и пишем в словарь
@dp.message_handler(state=FSMadmin.category_code)
async def select_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['category_code'] = message.text
        await FSMadmin.next()
        await message.answer('Введи code подкатегории:')


# Ловим четвертый ответ "code подкатегории" и пишем в словарь
@dp.message_handler(state=FSMadmin.subcategory_code)
async def select_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['subcategory_code'] = message.text
        await FSMadmin.next()
        await message.answer('Введи название товара:')


# Ловим пятый ответ "Название" и пишем в словарь
@dp.message_handler(state=FSMadmin.name)
async def select_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.answer('Загрузи фото:')


# Ловим шестой ответ "Фото" и пишем в словарь
@dp.message_handler(content_types=['photo'], state=FSMadmin.photo)
async def select_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.answer('Добавь описание:')


# Ловим седьмой ответ "Описание" и пишем в словарь
@dp.message_handler(state=FSMadmin.description)
async def select_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMadmin.next()
        await message.answer('Укажи цену:')


# Ловим восьмой ответ "Цена" и пишем в словарь
@dp.message_handler(state=FSMadmin.price)
async def select_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text.replace(',', '.'))
        await FSMadmin.next()
        await message.answer('Укажи количество:')


# Ловим девятый ответ "Количество", пишем в словарь и завершаем.
@dp.message_handler(state=FSMadmin.count)
async def select_count(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['count'] = int(message.text)

        res = data.values()
        r = list(res)
        print(r)
        category_name = r[0]
        subcategory_name = r[1]
        category_code = r[2]
        subcategory_code = r[3]
        name = r[4]
        photo = r[5]
        description = r[6]
        price = r[7]
        count = r[8]

        await commands.add_item(category_name=category_name, subcategory_name=subcategory_name,
                                category_code=category_code, subcategory_code=subcategory_code, name=name,
                                photo_id=photo, description=description, price=price, count=count)
        await state.finish()
        await message.bot.send_photo(chat_id=message.from_user.id,
                                     photo=f'{photo}',
                                     caption=f'<b>Вы успешно добавили товар:</b>\n\n'
                                             f'<b>Название:</b> {name}\n\n'
                                             f'<b>Описание:</b> {description}\n\n'
                                             f'<b>Наличие:</b> {count} шт.\n\n'
                                             f'<b>Цена:</b> {price} руб.\n\n'
                                     )
