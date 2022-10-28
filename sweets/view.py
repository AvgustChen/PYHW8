async def start_game(update):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
       Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\
       Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
       Все конфеты оппонента достаются сделавшему последний ход.')
async def help(update):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
       Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\
       Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
       Все конфеты оппонента достаются сделавшему последний ход.\n\n\
        /start - Начать игру сначала\n \
        /help - пощь по коммандам и правила игры')


async def table_info(update, name: str, count: int, total_count: int, name2: str):
    await update.message.reply_text(f'{name} взял {count} конфет\nИ на столе осталось {total_count} конфет\nХод {name2}\n\n Чтобы начать сначало введите /start')


async def wrong_take(update):
    await update.message.reply_text('Ты взял конфет больше чем нужно (или меньше)! Попробуй еще раз')


async def player_take(update):
    await update.message.reply_text('Возьмите конфеты, но не больше 28: ')


async def win(update, name:str):
    await update.message.reply_text(f'{name} выиграл! \n\n Чтобы начать игру заного введите /start')