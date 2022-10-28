from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler, filters
import controller, view

app = ApplicationBuilder().token("5303878052:AAHjyBSWFqsU0Hv238q0gVsX-WEtCQMsCp4").build()

app.add_handler(CommandHandler('start', view.start))
app.add_handler(CommandHandler('help', view.help))
app.add_handler(MessageHandler(filters.TEXT, controller.init_list))
app.run_polling(drop_pending_updates=True)


