from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/products')]],
                         resize_keyboard=True)


ikb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Korish', callback_data="db_get_all_products")],
                                            [InlineKeyboardButton(text='qoshish', callback_data="db_insert_product")]])

buy_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🛒', callback_data='savatchaga'),
         InlineKeyboardButton(text='❤', callback_data='sevimlilar')]

    ])
