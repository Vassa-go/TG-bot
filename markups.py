from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# navigation
btnBack = KeyboardButton("Вернуться назад")

# start
btnHelp = KeyboardButton("Помощь")
btnInfo = KeyboardButton("Информация")

StartBtns = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnHelp)

# helper
btnSite = KeyboardButton("Проблема с сайтом")

HelpMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSite, btnServer, btnHad, btnBack)

# inline post
btnInlinePost = InlineKeyboardButton(text="Написать на почту", url="")  # in url set gmail
btnInline = InlineKeyboardMarkup(row_width=1)
btnInline.insert(btnInlinePost)

# callback inline
btnYes = InlineKeyboardButton(text="Да", callback_data="Да")
btnNo = InlineKeyboardButton(text="Нет", callback_data="Нет")
AnswerMenu = InlineKeyboardMarkup(row_width=2)
AnswerMenu.insert(btnYes)
AnswerMenu.insert(btnNo)
