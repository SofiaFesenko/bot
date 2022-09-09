from settings import *

one = ['Сьогодні – ідеальний день для нових починань.',
       'Оптимальний день для того, щоб зважитися на сміливий вчинок!',
       'Будьте обережні, сьогодні зірки можуть вплинути на фінансовий стан.',
       'Найкращий час для того, щоб почати нові стосунки або розібратися зі старими',
       'Плідний день для того, щоб розібратися з справами, що накопичилися.']

two = ['Якщо поїдете за місто, заздалегідь подумайте про',
       'Але пам"ятайте, що навіть у цьому випадку не потрібно забувати про',
       'Ті, хто сьогодні націлений виконати безліч справ, повинні пам"ятати про',
       'Якщо у вас занепад сил, зверніть увагу на',
       'Пам"ятайте, що думки матеріальні, а значить вам протягом дня потрібно постійно думати про']

three = ['стосунки з друзями та близькими.',
         'роботу та ділові питання, які можуть так недоречно зашкодити планам.',
         'себе і своє здоров"я, інакше до вечора вам гаплик.',
         'побутові питання – особливо ті, які ви не доробили вчора.',
         'відпочинок, щоб не перетворитися на загнаного коня наприкінці місяця.']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "привіт":
        bot.send_message(message.from_user.id, "Привіт, {0.first_name}! \n Зараз я розкажу тобі гороскоп на сьогодні.".format(message.from_user))
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телець', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнюки', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Діва', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Терези', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпіон', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрілец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козеріг', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолій', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Риби', callback_data='zodiac')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Обери свій знак зодіаку', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привіт")
    else:
        bot.send_message(message.from_user.id, "Не розумію. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
        msg = random.choice(one) + ' ' + random.choice(two) + ' ' + random.choice(three)
        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)
