from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler, filters
import random
import view, model

app = ApplicationBuilder().token("5617585493:AAF4JQJMtp4gxsUp9UDjyZzEVaNHrHpzwKs").build()

async def start_game(update, context):
    await model.set_game()
    await view.start_game(update)
    name = update.effective_user.first_name
    await model.set_player_name(name)
    first_turn = random.randint(0,1)
    if first_turn:
        await view.player_take(update)
    else: await bot_turn(update, context)

async def player_turn(update, context):
    game = await model.get_game()
    if game:
        take = 0
        if update.message.text == '/start':
            return
        else:
            take = int(update.message.text)
        if (take <= 28) and (take > 0):
            await model.set_total_count(take)
        else:
            await view.wrong_take(update)
            return
        name = await model.get_player_name()
        total_count = await model.get_total_count()
        await view.table_info(update, name, take, total_count, 'Бот')
        if await model.get_total_count() > 0:
            await bot_turn(update,context)
        else:
            await view.win(update, 'Игрок')
            await model.set_game()

async def bot_turn(update,context):
    take = await model.bot_take()
    await model.set_total_count(take)
    name = await model.get_player_name()
    total_count = await model.get_total_count()
    await view.table_info(update, 'Бот', take, total_count, name)
    if await model.get_total_count() <= 0:
        await view.win(update, 'Бот')
        await model.set_game()

async def help(update, context):
    await view.help(update)

app.add_handler(CommandHandler('start', start_game))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.TEXT, player_turn))
app.run_polling(drop_pending_updates=True)