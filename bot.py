import logging
from aiogram import executor, types

from markups import StartBtns, HelpMenu, AnswerMenu, btnInline
from config import dp, bot

# log level
logging.basicConfig(level=logging.INFO)


# start bot
async def on_startup(_):
    print("Бот начал работу")


# start
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Добрый день!\nЧем мы можем Вам помочь?", reply_markup=StartBtns)


# dialog
@dp.message_handler()
async def office_address(message: types.Message):
    # navigation

    if message.text.lower() == "вернуться назад":
        await message.answer("Здесь Вы можете:\n-Узнать информацию о компании\n"
                             "-Решить свой вопрос через бота", reply_markup=StartBtns)

    if message.text.lower() == "помощь":
        await message.answer("Вы находитесь в разделе \"Помощь\"\nЧем мы можем Вам помочь?", reply_markup=HelpMenu)

    # start dialog
    if message.text.lower() == "информация":
        await message.answer("техническая поддержка")

    # helper
    if message.text.lower() == "проблема с сайтом":
        await message.answer("Попробуйте перезагрузить сайт\nМы помогли Вам найти решение проблемы?",
                             reply_markup=AnswerMenu)


# quiz
@dp.callback_query_handler()
async def answer_menu(call: types.CallbackQuery):
    if call.data == "Да":
        await bot.send_message(call.from_user.id, "Спасибо, что воспользовались нашим ботом!",
                               reply_markup=StartBtns)
    if call.data == "Нет":
        await bot.send_message(call.from_user.id, "Пожалуйста, напишите нам на почту"
                                                  " и мы постараемся разобраться с Вашей проблемой.",
                               reply_markup=btnInline)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # run long-polling
