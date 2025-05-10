import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Добро пожаловать в Кванториум!\n   \n"
                  "Я бот, который поможет вам узнать расписание групп.\n\n"
                  "🗓 Используйте следующие команды:\n"
                  "/check - Посмотреть расписание групп\n"
                  "/info - Узнать больше о Кванториуме\n"
                  "/help - Получить помощь по использованию бота\n\n")


@bot.message_handler(commands=['check'])
def check(message):
    keyboard = types.InlineKeyboardMarkup()
    it_check = types.InlineKeyboardButton(text='Энерджи-квантум', callback_data='it_course')
    auto_check = types.InlineKeyboardButton(text='Био-квантум', callback_data='bio')
    nano_check = types.InlineKeyboardButton(text='Нано-квантум', callback_data='nano-kv')
    keyboard.add(it_check, auto_check,nano_check )

    bot.send_message(message.chat.id, "Выберите курс:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def knopka(call):

    if call.data == 'it_course':

        keyboard = types.InlineKeyboardMarkup()
        group1_button = types.InlineKeyboardButton(text='Группа AB9', callback_data='group_AV9')
        group2_button = types.InlineKeyboardButton(text='Группа AB10', callback_data='group_AV10')
        group3_button = types.InlineKeyboardButton(text='Группа AB11', callback_data='group_AV11')
        group4_button = types.InlineKeyboardButton(text='Группа AB12', callback_data='group_AV12')
        group5_button = types.InlineKeyboardButton(text='Группа ОИ13', callback_data='group_oi13')
        group6_button = types.InlineKeyboardButton(text='Группа АВ19', callback_data='group_AV19')
        group7_button = types.InlineKeyboardButton(text='Группа ДШ3', callback_data='group_DH3')
        group8_button = types.InlineKeyboardButton(text='Группа ДШ2', callback_data='group_DH2')
        group9_button = types.InlineKeyboardButton(text='Цифровой дизайн', callback_data='Dis')

        keyboard.add(group1_button, group2_button,  group3_button,  group4_button, group5_button, group6_button, group7_button, group8_button, group9_button)

        bot.send_message(call.message.chat.id, "Выберите группу энерджи-квантум:", reply_markup=keyboard)

    elif call.data == 'bio':

        keyboard = types.InlineKeyboardMarkup()
        group1_button = types.InlineKeyboardButton(text='Группа Б3-C', callback_data='group_B3')
        group2_button = types.InlineKeyboardButton(text='Группа Б1-C', callback_data='group_B1')
        group3_button = types.InlineKeyboardButton(text='Группа Б2-C', callback_data='group_B2')
        group4_button = types.InlineKeyboardButton(text='Группа Б4-C', callback_data='group_B4')
        group5_button = types.InlineKeyboardButton(text='Группа Б5-C', callback_data='group_B5')
        group6_button = types.InlineKeyboardButton(text='Группа Б8-C', callback_data='group_B8_35')
        group7_button = types.InlineKeyboardButton(text='Группа Б9-C', callback_data='group_B9_35')


        keyboard.add(group1_button, group2_button, group3_button, group4_button, group5_button, group6_button, group7_button)

        bot.send_message(call.message.chat.id, "Выберите группу био-квантум:", reply_markup=keyboard)




    elif call.data == 'nano-kv':

        keyboard = types.InlineKeyboardMarkup()
        group1_button = types.InlineKeyboardButton(text='Группа Н5 сет. 35 школа', callback_data='group_n5')
        group2_button = types.InlineKeyboardButton(text='Группа Н6 сет. 35 школа', callback_data='group_n6')
        group3_button = types.InlineKeyboardButton(text='Группа Н2-С.', callback_data='group_n2')
        group4_button = types.InlineKeyboardButton(text='Группа Н1-С.', callback_data='group_n1')
        group5_button = types.InlineKeyboardButton(text='Группа Б6-Б.', callback_data='group_b6')
        group6_button = types.InlineKeyboardButton(text='Группа Н3-Б.', callback_data='group_n3')
        group7_button = types.InlineKeyboardButton(text='Группа Б7-С', callback_data='group_b7')
        group8_button = types.InlineKeyboardButton(text='Группа Н4-П', callback_data='group_n4')

        keyboard.add(group1_button, group2_button, group3_button, group4_button, group5_button, group6_button, group7_button, group8_button)
        bot.send_message(call.message.chat.id, "Выберите группу нано-квантум:", reply_markup=keyboard)


    elif call.data == 'group_n5':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Н5 сет. 35 школа\n"
                                               "(О.А.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 8:00 - 11:00\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 8:00- 11:00")


    elif call.data == 'group_n6':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Н6 сет. 35 школа\n"
                                               "(О.А.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 11:00 - 14:00\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 11:00 - 14:00")


    elif call.data == 'group_n2':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Н2-C\n"
                                               "12-14 лет (О.А.)\n\n"
                                               "📌Четверг\n"
                                               "⏰ 15:00 - 16:30\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 16:30 - 18:00")

    elif call.data == 'group_n1':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Н1-С.\n"
                                               "12-14 лет (О.А.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 15:00 - 16:30\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 15:00 - 16:30")


    elif call.data == 'group_b6':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Б6-Б.\n"
                                               "14-17 лет (Д.И.)\n\n"
                                               "📌Среда\n"
                                               "⏰ 16:30 - 18:00\n\n")


    elif call.data == 'group_n3':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Н3-Б.\n"
                                               "14-15 лет (О.А.)\n\n"
                                               "📌Четверг\n"
                                               "⏰ 16:30 - 18:00\n\n"
                                               "📌 Пятница\n"
                                               "⏰ 16:30 - 18:00")

    elif call.data == 'group_b7':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Б7-C.\n"
                                               "14-17 лет (Д.И.)\n\n"
                                               "📌Среда\n"
                                               "⏰ 18:00 - 19:30\n\n")


    elif call.data == 'group_n4':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Н4-П\n"
                                               "15 - 16 лет (О.А.)\n\n"
                                               "📌Четверг\n"
                                               "⏰ 18:00 - 19:30\n\n"
                                               "📌 Пятница\n"
                                               "⏰ 18:00 - 19:30")

    elif call.data == 'group_AV9':
        bot.send_message(call.message.chat.id, "📅 Расписание группы АВ9-С\n"
                                               "13-17 лет (А.А.)\n\n"
                                               "📌Вторник\n"
                                               "⏰ 15:00 - 16:30\n\n"
                                               "📌 Среда\n"
                                               "⏰ 15:00 - 16:30")


    elif call.data == 'group_AV10':
        bot.send_message(call.message.chat.id, "📅 Расписание группы АВ10-С\n"
                                               "13-17 лет (А.А.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 15:00 - 16:30\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 15:00 - 16:30")

    elif call.data == 'group_AV11':
        bot.send_message(call.message.chat.id, "📅 Расписание группы АВ11-С\n"
                                               "14-17 лет (А.А.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 16:30 - 18:00\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 16:30 - 18:00")


    elif call.data == 'group_AV12':
        bot.send_message(call.message.chat.id, "📅 Расписание группы АВ12-С\n"
                                               "14-17 лет (А.А.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 18:00 - 19:30\n\n"
                                               "📌 Суббота\n"
                                               "⏰ 18:00 - 19:30")

    elif call.data == 'group_oi13':
        bot.send_message(call.message.chat.id, "📅 Расписание группы ОИ13-С\n"
                                               "8-10 лет (В.Л.)\n\n"
                                               "📌Вторник\n"
                                               "⏰ 9:30 - 11:00\n\n"
                                               "📌 Четверг\n"
                                               "⏰ 9:30 - 11:00")

    elif call.data == 'group_AV19':
        bot.send_message(call.message.chat.id, "📅 Расписание группы АВ19-С\n"
                                               "НЕИЗВЕСТНО лет (А.А.)\n\n"
                                               "📌Суббота\n"
                                               "⏰ 11:00 - 12:30\n\n")



    elif call.data == 'group_DH3':
        bot.send_message(call.message.chat.id, "📅 Расписание группы ДШ3-С\n"
                                               "6-7 лет (Л.Г.)\n\n"
                                               "📌Вторник\n"
                                               "⏰ 16:30 - 18:00\n\n"
                                               "📌 Четверг\n"
                                               "⏰ 16:30 - 18:00")


    elif call.data == 'group_DH2':
        bot.send_message(call.message.chat.id, "📅 Расписание группы ДШ2-С\n"
                                               "5-6 лет (Л.Г.)\n\n"
                                               "📌Вторник\n"
                                               "⏰ 18:00 - 19:30\n\n"
                                               "📌 Четверг\n"
                                               "⏰ 18:00 - 19:30")



    elif call.data == 'Dis':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Цифровой дизайн\n"
                                               "НЕИЗВЕСТНО лет (НЕИЗВЕСТНО )\n\n"
                                               "📌Понедельник\n"
                                               "⏰ 18:00 - 19:30\n\n"
                                               "📌 Среда\n"
                                               "⏰ 18:00 - 19:30")




    elif call.data == 'group_B3':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Б3-С\n"
                                               "6-9 лет (Л.С.)\n\n"
                                               "📌Понедельник\n"
                                               "⏰ 9:30 - 11:00\n\n"
                                               "📌 Среда\n"
                                               "⏰ 9:30 - 11:00")
    elif call.data == 'group_B1':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Б1-С\n"
                                               "6-7 лет (Л.С.)\n\n"
                                               "📌Понедельник\n"
                                               "⏰ 15:00 - 16:30 \n\n"
                                               "📌 Среда\n"
                                               "⏰ 15:00 - 16:30")



    elif call.data == 'group_B2':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Б2-С\n"
                                               "8-9 лет (Л.С.)\n\n"
                                               "📌Понедельник\n"
                                               "⏰ 16:30 - 18:00 \n\n"
                                               "📌 Среда\n"
                                               "⏰ 15:00 - 16:30")

    elif call.data == 'group_B4':
        bot.send_message(call.message.chat.id, "📅 Расписание группы Б4-С\n"
                                               "12-15 лет (Е.В.)\n\n"
                                               "📌Четверг\n"
                                               "⏰ 16:30 - 18:00 ")



    elif call.data == 'group_B5':
        bot.send_message(call.message.chat.id, "📅 Расписание группы B5-С\n"
                                               "12-15 лет (Е.В.)\n\n"
                                               "📌Четверг\n"
                                               "⏰ 18:00 - 19:30 \n\n")



    elif call.data == 'group_B8_35':
        bot.send_message(call.message.chat.id, "📅 Расписание группы B8-С (35 Школа)\n"
                                               "(К.Э.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 11:00 - 14:00 \n\n"
                                               "📌 Суббота\n"
                                               "⏰ 11:00 - 14:00")

    elif call.data == 'group_B9_35':
        bot.send_message(call.message.chat.id, "📅 Расписание группы B8-С (35 Школа)\n"
                                               "(К.Э.)\n\n"
                                               "📌Пятница\n"
                                               "⏰ 12:00 - 13:30 \n\n"
                                               "📌 Суббота\n"
                                               "⏰ 12:00 - 13:30")





    bot.answer_callback_query(call.id)





@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Кванториум – федеральная сеть детских технопарков. \n\n"
                                      "Кванториум – это инновационные образовательные центры для детей и подростков, "
                                      "созданные в рамках федерального проекта 'Образование'. "
                                      "Их цель – вовлечь школьников в научно-техническое творчество, "
                                      "развить инженерные навыки и подготовить новое поколение специалистов для "
                                      "высокотехнологичных отраслей экономики. \n\n"
                                      "🔹 Основные направления обучения (квантумы)\n"
                                      "В каждом технопарке представлены несколько направлений (квантумов), среди которых:  \n"
                                      "- Промробоквантум – робототехника и автоматизированные системы.  \n"
                                      "- IT-квантум – программирование, кибербезопасность, искусственный интеллект.  \n"
                                      "- Аэроквантум – беспилотные летательные аппараты и авиамоделирование.  \n"
                                      "- Биоквантум – биотехнологии, генная инженерия, микробиология.  \n"
                                      "- Наноквантум – работа с наноматериалами и современными методами исследований.  \n"
                                      "- Энерджиквантум – альтернативная энергетика и возобновляемые источники.  \n"
                                      "- Хайтек – высокотехнологичная лаборатория с 3D-принтерами, лазерными станками и др.  \n\n"
                                      "🔹 Кто может обучаться?  \n"
                                      "Программы рассчитаны на школьников от 10 до 18 лет. Обучение бесплатное, набор проходит на конкурсной основе.  \n\n"
                                      "🔹 Где находятся Кванториумы?  \n"
                                      "Технопарки открыты более чем в 100 городах России, включая Москву, Санкт-Петербург, "
                                      "Казань, Новосибирск, Владивосток и др. "
                                      "Также существуют мобильные Кванториумы – передвижные лаборатории для детей из малых городов и сёл. \n\n"
                                      "🔹 Преимущества обучения  \n"
                                      "✅ Практико-ориентированный подход – работа над реальными проектами.  \n"
                                      "✅ Современное оборудование (3D-принтеры, VR-технологии, роботы).\n"
                                      "✅ Занятия ведут преподаватели-практики из наукоёмких отраслей.  \n"
                                      "✅ Возможность участия в олимпиадах, хакатонах и всероссийских конкурсах.  \n\n"
                                      "🔹 Как поступить?  \n"
                                      "Запись проходит через официальный сайт kvantorium.ru или региональные филиалы. Необходимо подать заявку и пройти отбор.  \n"
                                      "Кванториум – это отличная возможность для школьников получить актуальные навыки будущего и реализовать свои инженерные и научные идеи! 🚀   ")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     "💡 Доступные команды:\n"
                     "/start - Запуск/перезапуск бота\n"
                     "/check - Посмотреть расписание групп\n"
                     "/info - Узнать больше о Кванториуме\n"
                     "/help - Получить помощь по использованию бота")

bot.infinity_polling()

#код от ZTTao (Zenith Tech TAO)
# Версия: 1.3.4
