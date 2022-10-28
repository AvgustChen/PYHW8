from telegram import Update
import logger
import view

list = ''
result = ''
opSelect = {
    "*": lambda x, y: float(x) * float(y),
    "/": lambda x, y: float(x) / float(y),
    "+": lambda x, y: float(x) + float(y),
    "-": lambda x, y: float(x) - float(y)}

async def init_list(update, context):
    global list
    global result
    global opSelect
    await update.message.reply_text(f'Введите ваше выражение: ')
    list = str(update.message.text)
    await input_list(update, list)

# async def result_list(list):
#     global result
#     result = totalOperation(list)

async def input_list(update, list):
    if '/0' in list:
        await view.error_value_zerro(update)
    else:
        await totalOperation(update, list)

async def deleteElement(list, i):
    list.pop(i + 1)
    list.pop(i)

async def operation2(list, i, oper):
    if list[i] == oper:
        list[i - 1] = opSelect.get(oper)(float(list[i - 1]), float(list[i + 1]))
        await deleteElement(list, i)
        return True
    
async def totalOperation(update, list):
    list1 = list
    list = list.replace(' ', '').strip()
    list = list.replace('+', ' + ')\
        .replace('-', ' - ')\
        .replace('*', ' * ')\
        .replace('/', ' / ')
    list = list.split()
    

    while len(list)>1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if await operation2(list, i, '*'): break
                if await operation2(list, i, '/'): break

        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if await operation2(list, i, '+'): break
                if await operation2(list, i, '-'): break 
    result = 0  
    for i in list:
        result += i 


    await view.print_total(update, list1, result)
    logger.logger(f'{list1} = {list}')

      


    
