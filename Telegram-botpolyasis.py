from telebot import TeleBot
from telebot import types

bot = TeleBot('Bot_token')
h = 'http://clasevirtual.ru/index/alexander_un_dia_malo_muy_malo/0-174'
n = 'https://www.youtube.com/results?search_query=%E2%80%9C100+pel%C3%ADculas+en+espa%C3%B1ol%E2%80%9D'
m = 'https://animelon.com/video/63a12f239f75c625b0b80fb4'
u = 'https://anisub.tv/anime/super-cub'
i = 'https://9animetv.to/home'


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Which language would you like to learn?')
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton('English')
    btn2 = types.KeyboardButton('Spanish')
    markup.row(btn, btn2)
    btn3 = types.KeyboardButton('Chinese')
    btn4 = types.KeyboardButton('German')
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton('Japanese')
    markup.row(btn5)
    file = open('./english.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)


@bot.message_handler(content_types=["document"])
def handle_files(message):
    bot.send_message(message.chat.id, message.document)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    f = open('./Which_way.png', 'rb')
    if message.text == 'Chinese':
        bot.send_message(message.chat.id, 'What kind of materials are you interested in?')
        makeup = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Blogs')
        btn11 = types.KeyboardButton('Study book')
        btn12 = types.KeyboardButton('Movies/Series')
        makeup.add(btn, btn11)
        makeup.add(btn12)
        bot.send_photo(message.chat.id, f, reply_markup=makeup)
        bot.register_next_step_handler(message, china_case)
    elif message.text == 'English':
        bot.send_message(message.chat.id, 'What kind of materials are you interested in?')
        makeup2 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Blogs')
        btn11 = types.KeyboardButton('Study book')
        btn12 = types.KeyboardButton('Movies/Series')
        makeup2.row(btn, btn11)
        makeup2.row(btn12)
        bot.send_photo(message.chat.id, f, reply_markup=makeup2)
        bot.register_next_step_handler(message, english_case)
    elif message.text == 'German':
        bot.send_message(message.chat.id, 'What kind of materials are you interested in?')
        makeup3 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Blogs')
        btn11 = types.KeyboardButton('Study book')
        btn12 = types.KeyboardButton('Movies/Series')
        makeup3.row(btn, btn11)
        makeup3.row(btn12)
        bot.send_photo(message.chat.id, f, reply_markup=makeup3)
        bot.register_next_step_handler(message, german_case)
    elif message.text == 'Spanish':
        bot.send_message(message.chat.id, 'What kind of materials are you interested in?')
        makeup4 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Blogs')
        btn11 = types.KeyboardButton('Study book')
        btn12 = types.KeyboardButton('Movies/Series')
        makeup4.row(btn, btn11)
        makeup4.row(btn12)
        bot.send_photo(message.chat.id, f, reply_markup=makeup4)
        bot.register_next_step_handler(message, spanish_case)
    elif message.text == 'Japanese':
        bot.send_message(message.chat.id, 'What kind of materials are you interested in?')
        makeup4 = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Blogs')
        btn11 = types.KeyboardButton('Study book')
        btn12 = types.KeyboardButton('Movies/Series')
        makeup4.row(btn, btn11)
        makeup4.row(btn12)
        bot.send_photo(message.chat.id, f, reply_markup=makeup4)
        bot.register_next_step_handler(message, japanese_case)
    else:
        bot.send_message(message.chat.id, 'Should we try again?')
        markup3 = types.ReplyKeyboardMarkup()
        begin = types.KeyboardButton('/start')
        markup3.row(begin)


def china_case(message):
    if message.text == 'Study book':
        file1 = open('Chinese_A1.pdf', 'rb')
        bot.send_document(message.chat.id, document=file1, caption='I wish you luck!', timeout=20)
        bot.register_next_step_handler(message, start)
    elif message.text == 'Movies/Series':
        marky = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('I highly recommend! (use VPN)', url='https://www.bilibili.com/')
        button2 = types.InlineKeyboardButton('A lot of content(use Yandex)', url='https://www.youku.com/')
        button3 = types.InlineKeyboardButton('There is english subtitles',
                                             url='https://www.iq.com/play/new-life-begins-episode-1-it0z49ixrw?lang=en_us')
        button4 = types.InlineKeyboardButton('The good app for Androids',
                                             url='https://www.apkmonk.com/app/com.mightcast.vidfish/')
        marky.row(button, button2)
        marky.row(button3, button4)
        bot.send_message(message.chat.id, "Enjoy movies for free!", reply_markup=marky)


def english_case(message):
    if message.text == 'Study book':
        file1 = 'BQACAgIAAxkBAAIB22TUzY70AAHvPuw6RlbFtwQ-JDr9igACOTAAAqBRqEos2SyITQZERzAE'
        file2 = 'BQACAgIAAxkBAAIB3WTUzh2FM1xjnJyK2VWXYoHGh_4ZAAJAMAACoFGoSvtdkBiOumDCMAQ'
        file3 = 'BQACAgIAAxkBAAIB32TUzp1fnxRB9APrNnZ3_AbfVHJGAAJFMAACoFGoSo6LPiyOkHjjMAQ'
        file4 = 'BQACAgIAAxkBAAIB4WTUz_qCbzJj52nT3gQD1piSCyVXAAJLMAACoFGoStKBm0V3M-vMMAQ'
        file5 = 'BQACAgIAAxkBAAIByWTUxiEtuZLONgOLk7iMYAKATzkuAALfLwACoFGoSuQKHa7yf7YYMAQ'
        gig2 = {1: file1, 2: file2, 3: file3, 4: file4}
        for key in gig2:
            bot.send_document(message.chat.id, document=gig2[key], caption='Great choice!', timeout=40)
        bot.send_document(message.chat.id, document=file5, caption='Audio for you!')
    elif message.text == 'Movies/Series':
        marky = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Multiple languages!', url='https://moviesjoy.is/movie?page=4')
        button2 = types.InlineKeyboardButton('High quality', url='https://ymovies.vip/home/')
        marky.row(button, button2)
        bot.send_message(message.chat.id, "Enjoy movies for free!", reply_markup=marky)


def german_case(message):
    if message.text == 'Study book':
        file1 = open('Grammar_A1-A2.pdf', 'rb')
        file2 = open('Grammar_B1-B2.pdf', 'rb')
        file3 = open('Answers_A1-A2.pdf', 'rb')
        file4 = open('Answers_B1-B2.pdf', 'rb')
        file5 = open('Grammar_C1-C2.pdf', 'rb')
        file6 = open('Answers_C1-C2.pdf', 'rb')
        file7 = 'BQACAgIAAxkBAAIBy2TUy_9TUc4XiNaSbWNtVQPiKmxCAAIaMAACoFGoSm8F0kkavSP_MAQ'
        gig = {1: file1, 2: file2, 3: file3, 4: file4, 5: file5, 6: file6}
        for key in gig:
            bot.send_document(message.chat.id, document=gig[key], caption='It is gonna be awesome!', timeout=50)
        bot.send_document(message.chat.id, document=file7, caption='Don not forget about audios')
        bot.register_next_step_handler(message, start)


def spanish_case(message):
    if message.text == 'Study book':
        file11 = 'BQACAgIAAxkBAAIBpmTSMJvtnabGYhR6k_cwl3q1R_XXAAKGLQACtVGRSvgdJK26ltvhMAQ'
        file12 = 'BQACAgIAAxkBAAIBqGTSMd3TuYn6bVu_iccgREF0RLncAAKNLQACtVGRSkGuyuD7P4clMAQ'
        file13 = 'BQACAgIAAxkBAAIBqmTSMuHR-bB3DcFdinWrOOtz7cRaAAKSLQACtVGRSgoJjfV8plGeMAQ'
        file14 = 'BQACAgIAAxkBAAIBrGTSNMdgOVRFdMeG3s_sPskD4QaxAAKeLQACtVGRSpa1Cfy98hqZMAQ'
        file15 = 'BQACAgIAAxkBAAIBx2TUq55YkqRxeNrKFlXPtH_0bF7bAAKwLgACoFGoSpLU662tsAjDMAQ'
        gig = {1: file11, 2: file12, 3: file13, 4: file14}
        for key in gig:
            bot.send_document(message.chat.id, document=gig[key], caption='Language is a path to new opportunities!')
        bot.send_document(message.chat.id, document=file15, caption='Audio')
    elif message.text == 'Movies/Series':
        marky = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('The best variant (use VPN)', url=h)
        button2 = types.InlineKeyboardButton('On Youtube', url=n)
        marky.row(button, button2)
        bot.send_message(message.chat.id, "Train your skills with pleasure!", reply_markup=marky)


def japanese_case(message):
    if message.text == 'Study book':
        file11_id = 'BQACAgIAAxkBAAIBm2TRSRBTZTbIq9H4AnQvYoxpiTpPAAINNwACMDCISkT2XUbn-Hr8MAQ'
        file12_id = 'BQACAgIAAxkBAAIBmWTRRi-dFOG3522hDLR0krzN6ZVWAAL3NgACMDCISnAnOmO8bVl_MAQ'
        gig = {1: file11_id, 2: file12_id}
        for key in gig:
            bot.send_document(message.chat.id, document=gig[key], caption='I love this language too!', timeout=50)
    elif message.text == 'Movies/Series':
        marky2 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Anime in English!(without japanese subtitles', url=i)
        button2 = types.InlineKeyboardButton('Japanese subtitles!(without Russian)', url=m)
        button3 = types.InlineKeyboardButton('Translate everything you click on!', url=u)
        marky2.row(button, button2)
        marky2.row(button3)
        bot.send_message(message.chat.id, "Great Japanese content for you!", reply_markup=marky2)


bot.polling(none_stop=True, interval=0)
