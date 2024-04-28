import telebot
from telebot import types
bot = telebot.TeleBot('6374778219:AAH_1clLrFcrQRNUdtCGxxLMSUOKAx0_Oik')

@bot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь найти фильм?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Поиск', callback_data='yes')
  markup.add(button_yes)
  bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Напиши название в поиске"
        markup = types.InlineKeyboardMarkup()
        bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(function_call.id)
@bot.message_handler(content_types=["text"])
def text(message):
    if (message.text == 'Холоп') or (message.text == 'Холоп') or (message.text == 'Холоп 1') or (message.text == 'холоп 1') or (message.text == 'Холоп1') or (message.text == 'холоп1'):
        file1 = open('1.jpg', 'rb')
        opisanie="Холоп\n  \n27-летний московский мажор Григорий ошалел от безнаказанности. Богатый папа стабильно его отмазывает, да так, что уже обновил автопарк и оборудование отделению полиции, где служит начальником его друг. После очередной выходки терпение отца иссякает, и он обращается к психологу, практикующему шоковые методы воздействия на пациентов. Вскоре сынуля попадает в аварию и приходит в себя на деревенской конюшне. На дворе — Россия 1860 года, а сам он — бесправный конюх Гришка, которому за любую провинность и ослушание всегда готовы всыпать плетей, а то и вздёрнуть на глазах у всего честного народа."
        bot.send_photo(message.chat.id, file1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Скачать", url="https://cloud.mail.ru/public/Z9fF/f58b2LZUL"))
        bot.send_message(message.chat.id,opisanie, reply_markup=markup)
    elif (message.text == 'Холоп 2') or (message.text == 'холоп 2') or (message.text == 'Холоп2') or (message.text == 'холоп2'):
        file1 = open('2.webp', 'rb')
        opisanie = "Холоп 2\n  \nГриша, бывший мажор, побывавший холопом и ставший человеком, после путешествия в «прошлое» чутко реагирует на любую несправедливость. И, конечно, не может пройти мимо беспредела, который творит наглая и избалованная Катя. Ничего удивительного, что вскоре мажорка обнаруживает себя в другом времени.  "
        bot.send_photo(message.chat.id, file1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Скачать", url="https://cloud.mail.ru/public/jQKj/ELHvPAmBL"))
        bot.send_message(message.chat.id, opisanie, reply_markup=markup)
    elif message.text == 'Пищеблок':
        file1 = open('3.jpg', 'rb')
        opisanie = "Пищеблок \n  \nПока вся страна следит за Олимпиадой-80, в пионерском лагере «Буревестник» на Волге происходят странные события. Дети загадочно исчезают по ночам, а потом возвращаются — но совсем не такими, как прежде. Увлеченные летней свободой и друг другом вожатые не замечают, как в их отрядах оживают страшные пионерские легенды, а руководство лагеря делает вид, что все в порядке. Разбираться в тайнах «Буревестника» придется мальчику Валерке и вожатому Игорю. Для начала им предстоит понять, остался ли в лагере хоть кто-то, кому можно доверять."
        bot.send_photo(message.chat.id, file1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Скачать", url="https://cloud.mail.ru/public/jQKj/ELHvPAmBL"))
        bot.send_message(message.chat.id, opisanie, reply_markup=markup)
    elif message.text == 'Майор Гром: Чумной доктор':
        file1 = open('4.webp', 'rb')
        opisanie = "Майор Гром: Чумной доктор\n \nМайор полиции Игорь Гром известен всему Санкт-Петербургу пробивным характером и непримиримой позицией по отношению к преступникам всех мастей. Неимоверная сила, аналитический склад ума и неподкупность — всё это делает майора Грома идеальным полицейским. Но всё резко меняется с появлением человека в маске Чумного Доктора. Заявив, что его город «болен чумой беззакония», он принимается за «лечение», убивая людей, которые в своё время избежали наказания при помощи денег и влияния. Общество взбудоражено. Полиция бессильна. Игорь впервые сталкивается с трудностями в расследовании, от итогов которого может зависеть судьба всего города. "
        bot.send_photo(message.chat.id, file1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Скачать", url="https://cloud.mail.ru/public/SV9L/CpduMZKy5"))
        bot.send_message(message.chat.id, opisanie, reply_markup=markup)
    elif message.text == 'Рио':
        file1 = open('2.webp', 'rb')
        opisanie = ""
        bot.send_photo(message.chat.id, file1)
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Скачать", url="https://cloud.mail.ru/public/jQKj/ELHvPAmBL"))
        bot.send_message(message.chat.id, opisanie, reply_markup=markup)
    else:
        second_mess = "Такого фильма еще нет в наличии"
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, second_mess, reply_markup=markup)
        bot.answer_callback_query(message.chat.id)

bot.infinity_polling()
