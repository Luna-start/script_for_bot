from pyrogram import Client, filters
import re
from db import DataBase


db = DataBase('auto.db')
api_id = 27
api_hash = ''
phone = "+"

app = Client(name='my_accout', api_id=api_id, api_hash=api_hash, phone_number=phone)
# pattern = re.compile('SL\w+\s\|\s[^1-2]\'\d{3}\.?\d?\d?\sUAH\s\|\s-[^0]+\.\d\d%')
# pattern = re.compile('SL\w+\s\|\s[^1-2]\d+\'\d{3}\.?\d?\d?\sUAH\s\|\s\d+\.\d\d%')
# pattern2 = re.compile('SL\w+\s\|\s[^1-2]\'\d{3}\.?\d?\d?\sUAH\s\|\s-\d+%')
# pattern3 = re.compile('SL\w+\s\|\s[\d^1-2]\'\d{3}\.?\d?\d?\sUAH\s\|\s0%')
pattern4 = re.compile('SL\w+\s\|\s\d+\'\d{3}\.?\d?\d?\sUAH\s\|\s-[^0]+\.\d\d%')
pattern5 = re.compile('SL\w+\s\|\s\d+\'\d{3}\.?\d?\d?\sUAH\s\|\s-\d+%')
pattern6 = re.compile('SL\w+\s\|\s\d+\'\d{3}\.?\d?\d?\sUAH\s\|\s0%')
pattern7 = re.compile('SL\w+')

kill = 0

# @app.on_message()
# async def text_handler1(client, message):
#     global kill
#     print(message.text)

@app.on_message(filters.chat(7868))
async def text_handler(client, message):
    global kill
    print(message.text)
    if 'Купить код:' in message.text:
        kill = 0
        i = 0
        while kill == 0:
                try:
                    i +=1
                    print(i)
                    await client.request_callback_answer(
                        chat_id=message.chat.id,
                        message_id=message.id,
                        callback_data=message.reply_markup.inline_keyboard[1][0].callback_data
                    )
                except TimeoutError as e:
                    print(e)
                except OSError as e:
                    print(e)
    elif 'вы принимаете заявку' in message.text:
        kill = 1
        try:
            print(message.reply_markup.keyboard[0][1])
            await client.send_message(
                chat_id=message.chat.id,
                text=message.reply_markup.keyboard[0][1]
            )
        except TimeoutError as e:
            print(e)
        kill = 0
    elif 'По этой заявке уже' in message.text:
        try:
            print(message.reply_markup.keyboard[0][0])
            await client.send_message(
                chat_id=message.chat.id,
                text=message.reply_markup.keyboard[0][0]
            )
        except TimeoutError as e:
            print(e)
    elif 'Вы собираетесь покупать или продавать' in message.text:
        try:
            print(message.reply_markup.keyboard[0][0])
            await client.send_message(
                chat_id=message.chat.id,
                text=message.reply_markup.keyboard[0][0]
            )
        except TimeoutError as e:
            print(e)
    elif 'Сделка отклонена' in message.text:
        try:
            print(message.reply_markup.keyboard[0][0])
            await client.send_message(
                chat_id=message.chat.id,
                text=message.reply_markup.keyboard[0][0]
            )
        except TimeoutError as e:
            print(e)
    else:
        kill = 1




@app.on_edited_message(filters.chat(786))
async def text_handler(client, message):
    if "Купить код:" in message.text:
        sale = db.get_sale()
        if sale == 0:
            if re.search(pattern4, message.text):
                print(message.text, 4)
                full = re.search(pattern4, message.text)
                print(str(full.group(0)))
                match = re.search(pattern7, str(full))
                print(match)
                deal = str(match.group(0))
                await app.send_message(message.chat.id, f'/deal{deal}')
                print(deal)
            elif re.search(pattern5, message.text):
                print(message.text, 5)
                full = re.search(pattern5, message.text)
                print(str(full.group(0)))
                match = re.search(pattern7, str(full))
                print(match)
                deal = str(match.group(0))
                await app.send_message(message.chat.id, f'/deal{deal}')
                print(deal)
            elif re.search(pattern6, message.text):
                print(message.text, 6)
                full = re.search(pattern6, message.text)
                print(str(full.group(0)))
                match = re.search(pattern7, str(full))
                print(match)
                deal = str(match.group(0))
                await app.send_message(message.chat.id, f'/deal{deal}')
                print(deal)

        # if re.search(pattern, message.text):
        #     print(message.text, 1)
        #     full = re.search(pattern, message.text)
        #     print(str(full.group(0)))
        #     match = re.search(pattern7, str(full))
        #     print(match)
        #     deal = str(match.group(0))
        #     await app.send_message(message.chat.id, f'/deal{deal}')
        #     print(deal)
        # elif re.search(pattern2, message.text):
        #     print(message.text, 2)
        #     full = re.search(pattern2, message.text)
        #     print(str(full.group(0)))
        #     match = re.search(pattern7, str(full))
        #     print(match)
        #     deal = str(match.group(0))
        #     await app.send_message(message.chat.id, f'/deal{deal}')
        #     print(deal)
        # elif re.search(pattern3, message.text):
        #     print(message.text, 3)
        #     full = re.search(pattern3, message.text)
        #     print(str(full.group(0)))
        #     match = re.search(pattern7, str(full))
        #     print(match)
        #     deal = str(match.group(0))
        #     await app.send_message(message.chat.id, f'/deal{deal}')
        #     print(deal)
        if re.search(pattern4, message.text):
            print(message.text, 4)
            full = re.search(pattern4, message.text)
            print(str(full.group(0)))
            match = re.search(pattern7, str(full))
            print(match)
            deal = str(match.group(0))
            await app.send_message(message.chat.id, f'/deal{deal}')
            print(deal)
        elif re.search(pattern5, message.text):
            print(message.text, 5)
            full = re.search(pattern5, message.text)
            print(str(full.group(0)))
            match = re.search(pattern7, str(full))
            print(match)
            deal = str(match.group(0))
            await app.send_message(message.chat.id, f'/deal{deal}')
            print(deal)
        elif re.search(pattern6, message.text):
            print(message.text, 6)
            full = re.search(pattern6, message.text)
            print(str(full.group(0)))
            match = re.search(pattern7, str(full))
            print(match)
            deal = str(match.group(0))
            await app.send_message(message.chat.id, f'/deal{deal}')
            print(deal)
    else:
        pass



@app.on_message(filters.me)
async def admin(client, message):
    if message.text == '/admin_sale':
        sale = (await client.ask(message.chat.id, 'введите верхний %')).text
        try:
            await db.set_sale(int(sale))
        except:
            await app.send_message(message.chat.id, 'Ошибка')
        try:
            pattern4 = re.compile('SL\w+\s\|\s\d+\'\d{3}\.?\d?\d?\sUAH\s\|\s-[^0]+\.\d\d%')
    elif message.text == '/admin_amount':
        amount = (await client.ask(message.chat.id, 'введите минимальную сумму сделки')).text
        try:
            await db.set_amount(int(amount))
        except:
            await app.send_message(message.chat.id, 'Ошибка')


app.run()