import logging
from aiogram import Bot, Dispatcher, executor, types
import Database
import key
import config
import other

logging.basicConfig(level=logging.INFO)


db = Database.DateB()
bot = Bot(token=config.telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, db.get_hi_msg()[0][0], reply_markup=key.glav_key)
    video_url = db.get_hi_video()[0][0]
    await bot.send_video(message.from_user.id, video_url)
    db.add_user(message.from_user.id)


@dp.message_handler(content_types=['text'], text=['Полные лекции', 'Короткие видео', 'Ссылки, книги'])
async def obrab1(message: types.Message):
    if message.text == 'Полные лекции':
        await bot.send_message(message.from_user.id,
                               'Выберите тему:',
                               reply_markup=key.get_full_thems_keys())
    elif message.text == 'Короткие видео':
        await bot.send_message(message.from_user.id,
                               'Выберите тему: ',
                               reply_markup=key.get_short_thems_keys())
    elif message.text == 'Ссылки, книги':
        await bot.send_message(message.from_user.id,
                               db.get_other_resourses()[0][0])


@dp.callback_query_handler(lambda c: c.data in other.get_short_groups_for_lambda())
async def obrab_short_vids(call: types.CallbackQuery):
    videos = db.get_short_vidios(call.data[6:])
    if not videos:
        await bot.send_message(call.from_user.id, f'У нас нет коротких видео по теме - {call.data[6:]}: ')
    for vid in videos:
        try:
            await bot.send_message(call.from_user.id, f'Видео по теме - {call.data[6:]}')
            await bot.send_video(call.from_user.id, vid[0])
        except BaseException:
            logging.warning("Что то не так с отправкой короткого видео")


@dp.callback_query_handler(lambda c: c.data in other.get_long_groups_for_lambda())
async def obrab_short_vids(call: types.CallbackQuery):
    videos = db.get_long_vidios(call.data[5:])
    if not videos:
        await bot.send_message(call.from_user.id, f'У нас нет полных лекций по теме - {call.data[5:]}')
    else:
        for vid in videos:
            try:
                await bot.send_message(call.from_user.id, f'Видео по теме - {call.data[5:]}: ')
                await bot.send_video(call.from_user.id, vid[0])
            except BaseException:
                logging.warning("Что то не так с отправкой короткого видео")


@dp.message_handler(commands=['developer'])
async def developer(message: types.Message):
    await bot.send_message(message.from_user.id, 'Содатель данного бота - Бобёр\n'
                                                 'тг - @Georgiy1928\n'
                                                 'дс - go_gich#1098')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
