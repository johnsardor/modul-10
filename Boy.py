import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from commands import commands
from db import db_get_all_products, db_insert_product, create_table_users, insert_user
from keybords import kb, ikb, buy_ikb
from states import ProductStatesGroup, UserRegisterStatesGroup

load_dotenv()
Bot_token = os.getenv('BOT_TOKEN')
bot = Bot(token=Bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Assalomu Aleykum!\n Do'konimizga xush kelibsiz!\n"
                         "Iltimos ro'yxatdan o'ting /registration", reply_markup=kb)


@dp.message(Command('products'))
async def cmd_products(message: types.Message):
    await message.answer("Mahsulotlarni boshqarish", reply_markup=ikb)


@dp.message(Command('registration'))
async def cmd_registration(message: types.Message, state: FSMContext):
    await state.set_state(UserRegisterStatesGroup.full_name)
    await message.answer("Ism Familiya kiriting: ")


@dp.message(UserRegisterStatesGroup.full_name)
async def user_fullname(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(UserRegisterStatesGroup.phone)
    await message.answer("Telefon raqamingizni yuboring: ")


@dp.message(UserRegisterStatesGroup.phone)
async def user_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await insert_user(data["full_name"], data['phone'], message.from_user.id)
    await message.answer("Ro'yxatdan o'tdingiz! ")


@dp.callback_query(F.data == 'get_all_products')
async def get_all_products(call: types.CallbackQuery):
    products = get_all_products()
    await call.message.delete()
    if not products:
        await call.message.answer("Mahsulatlar mavjud emas")
    for product in products:
        print(product)
    await call.message.answer_photo(photo=product[3],
                                    caption=f"Mahsulot nime{product[1]}\n"
                                            f"Mahsulot narxi: {product[2]}\n",reply_markup=buy_ikb)


@dp.callback_query(F.data == 'add_product')
async def add_product(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(ProductStatesGroup.title)
    await call.message.answer("Mahsulotlarni nomini kiriting",reply_markup=kb)


@dp.message(ProductStatesGroup.title)
async def create_product_title(message: types.CallbackQuery, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(ProductStatesGroup.price)
    await message.answer("Mahsulotlarni narxini kiriting")


@dp.message(ProductStatesGroup.price)
async def create_product_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(ProductStatesGroup.photo)
    await message.answer("Mahsulotlar rasmini yubor")


@dp.message(ProductStatesGroup.photo)
async def update_product_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer("Mahsulot yaratildi")
    await db_insert_product(data['title'], data['price'], data['photo'])


async def main():
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
