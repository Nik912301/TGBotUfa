import telebot
from telebot import types
import config
import os.path

bot=telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    print(message.from_user.first_name, message.from_user.username, message.chat.id, message.text)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Конечно", callback_data='конечно')
    btn2 = types.InlineKeyboardButton("Нет", callback_data='нет')
    markup.add(btn1, btn2)

    media_group = []
    photo = ["https://sneg.top/uploads/posts/2023-04/thumbs/1680749376_sneg-top-p-ufa-kartinki-goroda-instagram-4.jpg"]

    for num in range(len(photo)):
        media_group.append(types.InputMediaPhoto(photo[num]))
    bot.send_media_group(message.chat.id,media_group)
    bot.send_message(message.chat.id,
                     'Привет! Я бот, который расскажет тебе о самых интересных достопримечательностях города Уфа. Готов отправиться в увлекательное путешествие по нашему прекрасному городу?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        markup = types.InlineKeyboardMarkup()
        if call.data == "конечно":
            btn1 = types.InlineKeyboardButton("1. Памятник Салавату Юлаеву", url="https://yandex.ru/maps/-/CDuwQQk1")
            btn2 = types.InlineKeyboardButton("2. Фонтан Семь девушек", url="https://yandex.ru/maps/-/CCU8MNdd8B")
            btn3 = types.InlineKeyboardButton("3. Уфимская мечеть-медресе Ляля-Тюльпан", url="https://yandex.ru/maps/-/CDuwQMMO")
            btn4 = types.InlineKeyboardButton("4. Уфа-Арена", url="https://yandex.ru/maps/-/CDuwQI7i")
            btn5 = types.InlineKeyboardButton("5. Монумент Дружбы", url="https://yandex.ru/maps/-/CDuwQE2P")
            btn6 = types.InlineKeyboardButton("6. Кафедральный соборный храм Рождества Богородицы", url="https://yandex.ru/maps/-/CDuwQA8R")
            btn7 = types.InlineKeyboardButton("Познакомься с историей Уфы", callback_data='история')
            markup.add(btn7)
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn6)

            media_group = []
            photo = [
                    os.path.realpath("sait/project_files/dost/1.jpg"),
                    os.path.realpath("sait/project_files/dost/2.jpg"),
                    os.path.realpath("sait/project_files/dost/3.jpg"),
                    os.path.realpath("sait/project_files/dost/4.jpg"),
                    os.path.realpath("sait/project_files/dost/5.jpg"),
                    os.path.realpath("sait/project_files/dost/6.jpg")]

            for num in range(len(photo)):
                media_group.append(types.InputMediaPhoto(open(photo[num], 'rb')))
            bot.send_media_group(call.message.chat.id, media_group)
            bot.send_message(call.message.chat.id,
                             'Добро пожаловать в Уфу! Этот город полон удивительных достопримечательностей, которые ты обязательно должен посетить.',
                             reply_markup=markup)

        elif  call.data == "история":
            btn1 = types.InlineKeyboardButton("<- вернуться назад", callback_data='конечно')
            btn2 = types.InlineKeyboardButton("1. Дом-музей С. Т. Аксакова, ок. 1750 г.", url="https://yandex.ru/maps/-/CDuwI89c")
            btn3 = types.InlineKeyboardButton("2. Демидовский дом, ок. 1770 г.", url="https://yandex.ru/maps/-/CDuwI-n9")
            btn4 = types.InlineKeyboardButton("3. Здание Дворянского собрания, ок. 1844–1856 гг.",url="https://yandex.ru/maps/-/CDuwMA1s")
            btn5 = types.InlineKeyboardButton("4. Покровская церковь, 1823 г.", url="https://yandex.ru/profile/-/CDuwMMPz")
            btn6 = types.InlineKeyboardButton("5. Гостиный двор, ок. 1820 г", url="https://yandex.ru/maps/-/CDuwMUzf")
            btn7 = types.InlineKeyboardButton("Исследуй природу", callback_data='природа')


            markup.add(btn1,btn7)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn6)

            media_group = []
            photo = [os.path.realpath("sait/project_files/history/_normal.jpg"),
                     os.path.realpath("sait/project_files/history/_normal (1).jpg"),
                     os.path.realpath("sait/project_files/history/_normal (2).jpg"),
                     os.path.realpath("sait/project_files/history/_normal (3).jpg"),
                     os.path.realpath("sait/project_files/history/_normal (4).jpg")]

            for num in range(len(photo)):
                media_group.append(types.InputMediaPhoto(open(photo[num], 'rb')))
            bot.send_media_group(call.message.chat.id, media_group)
            bot.send_message(call.message.chat.id,
                             'Познакомься с историей Уфы. Здесь ты найдешь множество исторических мест, таких как Уфимский кремль, который был построен в 16 веке.',
                             reply_markup=markup)

        elif  call.data == "природа":
            btn1 = types.InlineKeyboardButton("<- вернуться", callback_data='история')
            btn2 = types.InlineKeyboardButton("1. Парк имени Владимира Ленина", url="https://yandex.ru/maps/-/CDuwMBZ2")
            btn3 = types.InlineKeyboardButton("2. Парк имени лесоводов Башкирии", url="https://yandex.ru/maps/-/CDuwMF5F")
            btn4 = types.InlineKeyboardButton("3. Парк Победы", url="https://yandex.ru/maps/-/CDuwMJ4k")
            btn5 = types.InlineKeyboardButton("4. Софьюшкина аллея", url="https://yandex.ru/maps/-/CDuwMJNK")
            btn6 = types.InlineKeyboardButton("5. Сад культуры и отдыха имени Сергея Аксакова", url="https://yandex.ru/maps/-/CDuwMJ1S")
            btn7 = types.InlineKeyboardButton("Музеи и галереи", callback_data='музеи')
            markup.add(btn1, btn7)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn6)

            media_group = []
            photo = [os.path.realpath("sait/project_files/parks/_normal.jpg"),
                     os.path.realpath("sait/project_files/parks/_normal (1).jpg"),
                     os.path.realpath("sait/project_files/parks/_normal (2).jpg"),
                     os.path.realpath("sait/project_files/parks/_normal (3).jpg"),
                     os.path.realpath("sait/project_files/parks/_normal (4).jpg")]

            for num in range(len(photo)):
                media_group.append(types.InputMediaPhoto(open(photo[num], 'rb')))
            bot.send_media_group(call.message.chat.id, media_group)
            bot.send_message(call.message.chat.id,
                             'Исследуй природу Уфы. Город окружен красивыми парками и садами, где ты сможешь насладиться природой и провести время на свежем воздухе.',
                             reply_markup=markup)

        elif call.data == "музеи":
            btn1 = types.InlineKeyboardButton("<- вернуться", callback_data='природа')
            btn2 = types.InlineKeyboardButton("1. Музей Республики Башкортостан", url="https://yandex.ru/maps/-/CDuwM8MH")
            btn3 = types.InlineKeyboardButton("2. Художественный музей имени Михаила Васильевича Нестерова", url="https://yandex.ru/maps/-/CDuwM86b")
            btn4 = types.InlineKeyboardButton("3. Музей Боевой Славы", url="https://yandex.ru/maps/-/CDuwM8Kg")
            btn5 = types.InlineKeyboardButton("4. Музей археологии и этнографии им. Р.Г. Кузеева", url="https://yandex.ru/maps/-/CDuwM8oR")
            btn6 = types.InlineKeyboardButton("5. Дом-музей С.Т. Аксакова", url="https://yandex.ru/maps/-/CDuwM83~")
            btn7 = types.InlineKeyboardButton("Местная кухня.", callback_data='кухня')
            markup.add(btn1, btn7)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn6)

            media_group = []
            photo = [os.path.realpath("sait/project_files/museums/1.jpg"),
                     os.path.realpath("sait/project_files/museums/2.jpg"),
                     os.path.realpath("sait/project_files/museums/3.jpg"),
                     os.path.realpath("sait/project_files/museums/4.jpg"),
                     os.path.realpath("sait/project_files/museums/5.png")]

            for num in range(len(photo)):
                media_group.append(types.InputMediaPhoto(open(photo[num], 'rb')))
            bot.send_media_group(call.message.chat.id, media_group)
            bot.send_message(call.message.chat.id,
                             'Посети музеи и галереи. Уфа предлагает множество музеев и галерей, где ты сможешь узнать больше о культуре и искусстве этого региона.',
                             reply_markup=markup)

        elif call.data == "кухня":
            btn1 = types.InlineKeyboardButton("<- вернуться", callback_data='музеи')
            btn2 = types.InlineKeyboardButton("1. Ресторан «Азык-Тулек»", url="https://yandex.ru/maps/-/CDuwMLJB")
            btn3 = types.InlineKeyboardButton("2. Ресторан «Башкирия»", url="https://yandex.ru/maps/-/CDuwMLJB")
            btn4 = types.InlineKeyboardButton("3. Ресторан «Aibat Hallyar»", url="https://yandex.ru/maps/-/CDuwMPj5")
            btn5 = types.InlineKeyboardButton("4. Ресторан «Honey»", url="https://yandex.ru/maps/-/CDuwMPLG")
            btn6 = types.InlineKeyboardButton("5. Ресторан «Kumpan Cafe»", url="https://yandex.ru/maps/172/ufa/chain/kumpan/3953616660/filter/chain_id/3953616660/?ll=55.947984%2C54.726480&sctx=ZAAAAAgBEAAaKAoSCQZ%2Fv5gt%2B0tAEfbv%2BsxZW0tAEhIJ9aJ2vwrwjT8R2LlpM05DdD8iBgABAgMEBSgKOABAkc0GSAFqAnJ1nQHNzEw9oAEAqAEAvQFFrhV9wgEbhouxsQTf0tKpxwWf1%2B2fugW4tYLBBPO1hsMG6gEA8gEA%2BAEAggIZKChjaGFpbl9pZDooMzk1MzYxNjY2MCkpKYoCAJICAJoCDGRlc2t0b3AtbWFwc6oCPDM5NTM2MTY2NjAsNDkzOTQ3MTYxMzcsMjQwMDg1NzAxNTEzLDIyNjAzODU0OTgyNywxNzA3MTUzODI1ObACAQ%3D%3D&sll=55.947984%2C54.726480&sspn=0.116946%2C0.039566&z=14.01")
            markup.add(btn1)
            markup.add(btn2)
            markup.add(btn3)
            markup.add(btn4)
            markup.add(btn5)
            markup.add(btn6)

            media_group = []
            photo = [os.path.realpath("sait/project_files/kitchen/_normal.jpg"),
                     os.path.realpath("sait/project_files/kitchen/_normal (1).jpg"),
                     os.path.realpath("sait/project_files/kitchen/_normal (2).jpg"),
                     os.path.realpath("sait/project_files/kitchen/_normal (3).jpg"),
                     os.path.realpath("sait/project_files/kitchen/_normal (4).jpg")]

            for num in range(len(photo)):
                media_group.append(types.InputMediaPhoto(open(photo[num], 'rb')))
            bot.send_media_group(call.message.chat.id, media_group)
            bot.send_message(call.message.chat.id,
                             'Отведай местную кухню. Не забудь попробовать национальные блюда Уфы, такие как шурпа, беляши и чак-чак.',
                             reply_markup=markup)

        elif call.data == "нет":
            bot.send_message(call.message.chat.id, '😢')

bot.polling(none_stop=True)