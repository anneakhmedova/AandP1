elif message.text == 'Холоп 2':
    file1 = open('2.webp', 'rb')
opisanie = ""
bot.send_photo(message.chat.id, file1)
markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton("Скачать", url="https://cloud.mail.ru/public/jQKj/ELHvPAmBL"))
bot.send_message(message.chat.id, opisanie, reply_markup=markup)
