import logger


async def start(update, context):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
       Я бот калькулятор, который с легкостью сосчитает ваше выражение.\n Введите ваше выражение: ')

async def help(update, context):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n\
       Для того чтобы я сосчитал ваше выражение, введите его без знака =, например 2*4/6')

async def error_value(update):
    logger.logger('Ошибка ввода данных')
    await update.message.reply_text('Ошибка ввода данных')

async def error_value_zerro(update):
    logger.logger('Ошибка ввода данных')
    await update.message.reply_text('На ноль делить нельзя! Ошибка ввода данных')

async def print_total(update, list1, result):
    await update.message.reply_text(f'Результат: {list1} ={result}')
