import telepot, time
chave = '409627287:AAG27_mbwObUDjdh6NZFgbSF64SuT0LKce8'

def new_contact(message):
    bot = telepot.Bot('409627287:AAG27_mbwObUDjdh6NZFgbSF64SuT0LKce8')
    chat_id = '360807543'
    bot.sendMessage(chat_id, message)


new_contact('Pegue o pombo!')
