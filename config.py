import telebot 

from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def welcome(message):
        markup = types.ReplyKeyboardMarkup (resize_keyboard = True)
        item1 = types.KeyboardButton("Я новичок")
        item2 = types.KeyboardButton("Я стажер")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Привет, {0.first_name}!\n Я - {1.first_name}, персональный помощник для сотрудников компании. Если ты новичок, то нажми кнопку 'Я новичок!' и я выдам тебе все полезные материалы для прохождения твоей стажировки. Если тебе нужна помощь и ты хочешь оставить комментарии, то нажми 'Я стажер'." .format(message.from_user, bot.get_me()), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Я новичок':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Правила и документы", callback_data='protocol and documents')
            item2 = types.InlineKeyboardButton("Ссылки", callback_data='URL' )
            
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Хорошо, здесь ты можешь получить информации о стажировке: правила, какие документы нужны и как стажировка проходит. Также, я собрал все ссылки, которые тебе нужны в начале, чтобы войти в рабочий процесс. ", reply_markup=markup)

        elif message.text == 'Я стажер':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Жалоба", callback_data='complaint')
            item2 = types.InlineKeyboardButton("Пожелание", callback_data='wishes')
            
            
            markup.add(item1, item2, )
 
            bot.send_message(message.chat.id, 'ОБРАТИ ВНИМАНИЕ, ЧТО ты попал на вкладку для уже стажеров! Если ты еще не стажер, то нажми на кнопку "я новичок" ', reply_markup=markup)
   
        
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'protocol and documents':
                bot.send_message(call.message.chat.id, 'Итак, сейчас я тебе расскажу как будет проходить твоя стажировка. Но для начала давай определимся в какой команде ты хочешь стажироваться. У нас есть 3 команды: marketing, finance, product. В низ 3 разных руководителя. Каждая команда занимается своими задачами. Маркетинг - продвижением, Финансы - поиском инвестиций и фин.моделью, Продуктовая команда - управление IT продуктом Edwica. Ты можешь выбрать одну из трёх команд.\n Первым делом, после попадания в команду тебя ждет испытательный срок в течении месяца. Потом мы заключаем с тобой договор о стажировке. Напоминаю, что стажировка бессрочная. Помимо договора о стажировке мы также заключаем с тобой договор NDA - о неразглашении коммерческой тайны. Для оформления стажировки тебе понадобятся следующие документы:\n 1) Пасспортные данные\n 2) Номер СНИЛС\n 3)Твое желание стажироваться ;)\n !!!ВНИМАНИЕ!!! Стажировка НЕ оплачиваемая.\n Также в любой нашей команде есть правила:\n Во-первых, каждый будний день команда проводит созвон по Whats App со своим руководителем. На созвоны опаздывать и не появляться - запрещено! Если на созвон никак не получается присоединиться, то об этом следует заранее предупредить руководителя.\n Во-вторых, у вас есть доступ к коммерческой тайне, а значит ее надо хранить в секрете и относится к этому крайне серьезно. В-третьих, выполнять задачи в намеченных срок и усердно трудится.\n Также для работы тебе понадобятся некоторые наши ссылки. Нажми на кнопку "ссылки" и дальше я тебе все расскажу ')
            elif call.data == 'URL':
                bot.send_message(call.message.chat.id, ' 1. База знаний. Тут собрана вся инфа по Эдвике: ЦА, модель монетизации, фин модель, MVP, партнёры, конкуренты и т.д. Кстати, в инструментах есть ссылка на Geekbrains по тому, как работать в Figmа. Ссылка:\n https://www.notion.so/55739fcadb6445dca9509e355dcdd4c8,  Основной сайт маркетплейса Эдвика - ссылка:\n https://edwica.ru\n Социальные сети Эдвики:\n вк: https://vk.com/edwica\n инст: https://instagram.com/edwica_ru?utm_medium=copy_link\n Гугл диск для хранения всех доков - ссылка:\n https://drive.google.com/drive/folders/1Ly9R6OSMHAS0f..\n Figma, тут отрисовываем картинки для постов, чек-листов и тд. - ссылка:\n https://www.figma.com/file/5uxm23qJsVjSSMdUSoKU5U/Соц..\n Trello, все задачи отображаются там на доске - ссылка:\n https://trello.com/invite/b/He1sDIWM/1047018ac1f9c6c0..\n Установка шрифтов:\n https://drive.google.com/file/d/1ng8OaxDA_ghrlPiFIgIkC9-BnkkZwFGR/view?usp=sharing')

            #кнопки выбора направления по ЕГЭ для школьников
            if call.data == 'complaint':
                bot.send_message(call.message.chat.id, "Уважаемый наш стажер, мы уважаем друг друга, и хотим, чтобы в нашей организации была исключительно рабочая атмосфера! Поэтому перед тем как разместить жалобу в документе по ссылке, хорошо подумай, насколько она серьезна, потому что мы будем разбираться с этим!\n Ссылка: https://docs.google.com/spreadsheets/d/1QLFOhEdlsvHzS5LuvSlSngn8yOaMhtqsXKoHTg9Qdek/edit?usp=sharing ")
            
            #кнопки выбора направления по саморазвитию для школьников
            if call.data == 'wishes':
                bot.send_message(call.message.chat.id, 'Мы серьезно относимся ко всем нашим стажерам и нам не безразлично ваши пожелания.\n Все твои пожелания ты можешь оставить здесь: https://docs.google.com/spreadsheets/d/1AGxO7aROjxnKhxw0XpOrLL5tTNr5HyzUt32UBZKjZ9k/edit?usp=sharing')

            # remove inline buttons
            
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Нашёл!")


    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
