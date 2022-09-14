from distutils.command.config import config
from logging import disable
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

bot = Bot(token=config.TOKEN) #Ваш токен
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_answer(message: types.Message):
    await message.answer("👋 <b>Привіт,</b> <b>я Ваш Інформаційний Бот.</b> \n🪪 <b>Я напишу твою інформацію в Telegram.</b> \n📚 <b>Напишіть команду /information.</b>", parse_mode="HTML")
    
@dp.message_handler(commands=['information'])
async def cmd_answer(message: types.Message):
    name = message.from_user.full_name
    username = message.from_user.username
    username = username and f"@{username}"
    id = message.from_user.id
    link = message.from_user.username
    link = link and f"https://t.me/{link}"
    await bot.send_message(message.from_user.id, f"👤 <b>І'мя :</b> <b>{name}</b>\n🔑 <b>Ім'я користувача :</b> <b>{username  if username  else None}</b>\n💳 <b>Телеграм ID :</b> <b>{id}</b> \n🔗 <b>Посилання :</b> <b><a href='tg://user?id={id}'>{link if link else 'Ваше посилання'}</a></b>", parse_mode="HTML")

@dp.message_handler(commands=['help'])
async def cmd_answer(message: types.Message):
    await message.answer("⁉️<b> Якщо у вас є проблеми.</b> \n✉️ <b>Напишіть мені</b> <a href='https://t.me/nikit0ns'>@nikitons</a><b>.</b>", disable_web_page_preview=True, parse_mode="HTML")
    


if __name__ == '__main__':
    executor.start_polling(dp)