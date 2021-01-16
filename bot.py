import amino
import random


client = amino.Client()
client.login(email='a0apert@ya.ru', password='moscow22')
subs = client.sub_clients()

subclient = amino.SubClient(comId=subs.comId[0], profile=client.profile)

@client.callbacks.event("on_text_message")
def on_text_message(data):
    if data.message.content == '/help':
        mmes = 'Я бот Mentry.\nДоступные команды:\n/help - показать это сообщение\n/bless - получить благословение'
        subclient.send_message(chatId=data.message.chatId, message=mmes, replyTo=data.message.messageId)
    if data.message.content == '/bless':
        mmes = 'Светлые силы благословили тебя'
        if random.randint(0, 1) == 0:
            mmes = 'Тёмные силы благословили тебя'
        subclient.send_message(chatId=data.message.chatId, message=mmes, replyTo=data.message.messageId)
